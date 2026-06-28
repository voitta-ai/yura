"""Server-rendered SVG charts in the McKinsey exhibit idiom.

One accent color, no gridlines, data labels sit on the marks, generous
whitespace. Each function returns an SVG string to drop into a template
(rendered with the |safe filter).
"""
from __future__ import annotations

from html import escape

# --- design tokens (mirrors static/css/app.css) ---
NAVY = "#051C2C"
NAVY_SOFT = "#2A4A5E"
CYAN = "#00A9F4"
CYAN_SOFT = "#9AD9F5"
GRID = "#E6E6E6"
INK = "#1A1A1A"
MUTE = "#7A7A7A"

_FONT = "Helvetica Neue, Arial, sans-serif"


def _fmt(n: float) -> str:
    n = round(n)
    if abs(n) >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if abs(n) >= 1_000:
        return f"{n / 1_000:.1f}k"
    return f"{int(n)}"


def hbar(
    items: list[dict],
    *,
    width: int = 640,
    label_w: int = 168,
    bar_h: int = 26,
    gap: int = 12,
    highlight_first: bool = True,
    value_suffix: str = "",
) -> str:
    """Horizontal bar chart. items: [{label, value, sub?}]. First bar accented."""
    if not items:
        return _empty(width, 80)
    pad_t, pad_b, pad_r = 8, 8, 56
    plot_w = width - label_w - pad_r
    maxv = max((it["value"] for it in items), default=0) or 1
    height = pad_t + pad_b + len(items) * (bar_h + gap) - gap

    rows = []
    y = pad_t
    for i, it in enumerate(items):
        val = it["value"]
        bw = max(2, plot_w * (val / maxv))
        color = CYAN if (highlight_first and i == 0) else NAVY
        label = escape(str(it["label"]))
        sub = escape(str(it.get("sub", "")))
        cy = y + bar_h / 2
        rows.append(
            f'<text x="{label_w - 10}" y="{cy}" text-anchor="end" '
            f'dominant-baseline="central" font-size="12.5" fill="{INK}" '
            f'font-family="{_FONT}">{label}</text>'
        )
        if sub:
            rows.append(
                f'<text x="{label_w - 10}" y="{cy + 13}" text-anchor="end" '
                f'font-size="9.5" fill="{MUTE}" font-family="{_FONT}">{sub}</text>'
            )
        rows.append(
            f'<rect x="{label_w}" y="{y}" width="{bw:.1f}" height="{bar_h}" '
            f'fill="{color}" rx="1"/>'
        )
        rows.append(
            f'<text x="{label_w + bw + 8:.1f}" y="{cy}" dominant-baseline="central" '
            f'font-size="12" font-weight="700" fill="{NAVY}" '
            f'font-family="{_FONT}">{_fmt(val)}{escape(value_suffix)}</text>'
        )
        y += bar_h + gap

    return _svg(width, height, "".join(rows))


# Palette for segmented-bar series, applied in key order.
_SEG_COLORS = [NAVY, NAVY_SOFT, CYAN, "#5B8DB8", CYAN_SOFT]


def grouped_score(items: list[dict], *, width: int = 640) -> str:
    """Score breakdown: one row per item, a thin segmented bar per value key.

    Segments are derived from the first item's `values` keys, so this renders
    both the composite breakdown (volume/consistency/quality) and the RACE
    profile (readability/maintainability/correctness/efficiency).
    """
    if not items:
        return _empty(width, 80)
    keys = list(items[0]["values"].keys())
    seg = [(k, _SEG_COLORS[i % len(_SEG_COLORS)]) for i, k in enumerate(keys)]
    label_w, bar_h, gap, pad = 168, 9, 5, 10
    row_h = len(seg) * (bar_h + 3) + gap + 8
    plot_w = width - label_w - 48
    height = pad * 2 + len(items) * row_h

    rows = []
    y = pad
    for it in items:
        rows.append(
            f'<text x="{label_w - 10}" y="{y + 10}" text-anchor="end" '
            f'font-size="12.5" fill="{INK}" font-family="{_FONT}">'
            f'{escape(str(it["label"]))}</text>'
        )
        yy = y
        for key, color in seg:
            v = it["values"].get(key, 0)
            bw = max(1, plot_w * (v / 100))
            rows.append(
                f'<rect x="{label_w}" y="{yy}" width="{bw:.1f}" height="{bar_h}" '
                f'fill="{color}" rx="1"/>'
            )
            rows.append(
                f'<text x="{label_w + bw + 6:.1f}" y="{yy + bar_h - 1}" '
                f'font-size="8.5" fill="{MUTE}" font-family="{_FONT}">'
                f'{v:.0f}</text>'
            )
            yy += bar_h + 3
        y += row_h

    legend = _legend([(k.capitalize(), c) for k, c in seg], width)
    return _svg(width, height, "".join(rows)) + legend


def line(labels: list[str], values: list[int], *, width: int = 640, height: int = 220) -> str:
    """Single-series area+line, McKinsey-clean: no gridlines, sparse x ticks."""
    if not values:
        return _empty(width, height)
    pad_l, pad_r, pad_t, pad_b = 8, 16, 14, 28
    plot_w = width - pad_l - pad_r
    plot_h = height - pad_t - pad_b
    maxv = max(values) or 1
    n = len(values)

    def px(i: int) -> float:
        return pad_l + (plot_w * (i / (n - 1)) if n > 1 else plot_w / 2)

    def py(v: int) -> float:
        return pad_t + plot_h * (1 - v / maxv)

    pts = [(px(i), py(v)) for i, v in enumerate(values)]
    line_d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    area_d = (
        f"M{pts[0][0]:.1f},{pad_t + plot_h:.1f} "
        + " ".join(f"L{x:.1f},{y:.1f}" for x, y in pts)
        + f" L{pts[-1][0]:.1f},{pad_t + plot_h:.1f} Z"
    )

    parts = [
        f'<line x1="{pad_l}" y1="{pad_t + plot_h:.1f}" x2="{width - pad_r}" '
        f'y2="{pad_t + plot_h:.1f}" stroke="{GRID}" stroke-width="1"/>',
        f'<path d="{area_d}" fill="{CYAN}" opacity="0.10"/>',
        f'<path d="{line_d}" fill="none" stroke="{NAVY}" stroke-width="2"/>',
    ]
    # Peak marker.
    peak_i = max(range(n), key=lambda i: values[i])
    parts.append(
        f'<circle cx="{px(peak_i):.1f}" cy="{py(values[peak_i]):.1f}" r="3.5" '
        f'fill="{CYAN}"/>'
    )
    parts.append(
        f'<text x="{px(peak_i):.1f}" y="{py(values[peak_i]) - 8:.1f}" '
        f'text-anchor="middle" font-size="10" font-weight="700" fill="{NAVY}" '
        f'font-family="{_FONT}">{values[peak_i]}</text>'
    )
    # Sparse x labels: first, peak, last (avoid clutter).
    show = sorted({0, n - 1, peak_i})
    for i in show:
        parts.append(
            f'<text x="{px(i):.1f}" y="{height - 8}" text-anchor="middle" '
            f'font-size="9.5" fill="{MUTE}" font-family="{_FONT}">'
            f'{escape(labels[i])}</text>'
        )
    return _svg(width, height, "".join(parts))


def _median(xs: list[float]) -> float:
    s = sorted(xs)
    n = len(s)
    if not n:
        return 0.0
    mid = n // 2
    return s[mid] if n % 2 else (s[mid - 1] + s[mid]) / 2


def _axis_mapper(vals: list[float], scale: str, zoom: bool, clamp):
    """Return (to_frac, lo_data, hi_data): map a data value to a 0..1 fraction.

    scale="log" spreads long-tailed counts (commits, churn) via log1p; "linear"
    is plain. zoom=True frames a percent-like axis to its data band (with
    headroom) so clustered scores separate. clamp=(lo,hi) bounds the domain.
    """
    import math

    if scale == "log":
        hi = (math.log1p(max((max(v, 0.0) for v in vals), default=0.0)) * 1.05) or 1.0
        return (lambda v: math.log1p(max(0.0, v)) / hi), 0.0, math.expm1(hi)

    vmax = max(vals, default=1.0)
    vmin = min(vals, default=0.0)
    if zoom:
        pad = max(6.0, (vmax - vmin) * 0.15)
        lo_d, hi_d = vmin - pad, vmax + pad
    else:
        lo_d, hi_d = 0.0, (vmax * 1.05 or 1.0)
    if clamp:
        lo_d, hi_d = max(clamp[0], lo_d), min(clamp[1], hi_d)
    span = (hi_d - lo_d) or 1.0
    return (lambda v: (v - lo_d) / span), lo_d, hi_d


def scatter(
    items: list[dict],
    *,
    x_title: str,
    y_title: str,
    x_scale: str = "linear",
    y_scale: str = "linear",
    x_zoom: bool = False,
    y_zoom: bool = False,
    x_clamp=None,
    y_clamp=None,
    quadrants=None,
    tint=("tr", CYAN, "bl", NAVY),
    width: int = 680,
    height: int = 520,
) -> str:
    """McKinsey 2x2 bubble scatter — the general engine behind the hero matrix.

    items: [{x, y, size, label, highlight?}]. A median crosshair splits the
    field into four quadrants; quadrants={"tr","tl","br","bl"} labels the
    corners. Bubble area ∝ size (sqrt radius). tint shades a "good" and a "bad"
    corner faintly — pass tint=None to disable, or ("tl", CYAN, "br", NAVY) to
    move the shading when the desirable corner isn't top-right.
    """
    if not items:
        return _empty(width, height)
    pad_l, pad_r, pad_t, pad_b = 60, 120, 50, 56
    pw = width - pad_l - pad_r
    ph = height - pad_t - pad_b

    xs = [it["x"] for it in items]
    ys = [it["y"] for it in items]
    sizes = [max(1.0, it.get("size", 1)) for it in items]
    xf, xlo, xhi = _axis_mapper(xs, x_scale, x_zoom, x_clamp)
    yf, ylo, yhi = _axis_mapper(ys, y_scale, y_zoom, y_clamp)

    def px(v: float) -> float:
        return pad_l + pw * xf(v)

    def py(v: float) -> float:
        return pad_t + ph * (1 - yf(v))

    smax = max(sizes)
    def radius(s: float) -> float:
        return 7 + 22 * (s / smax) ** 0.5

    mx, my = px(_median(xs)), py(_median(ys))

    corners = {
        "tr": (mx, pad_t, pad_l + pw - mx, my - pad_t),
        "tl": (pad_l, pad_t, mx - pad_l, my - pad_t),
        "br": (mx, my, pad_l + pw - mx, pad_t + ph - my),
        "bl": (pad_l, my, mx - pad_l, pad_t + ph - my),
    }

    p = []
    # faint quadrant tints
    if tint:
        c1, col1, c2, col2 = tint
        for corner, col, op in ((c1, col1, 0.05), (c2, col2, 0.04)):
            x, y, w, h = corners[corner]
            p.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{max(0,w):.0f}" height="{max(0,h):.0f}" fill="{col}" opacity="{op}"/>')
    # frame
    p.append(f'<rect x="{pad_l}" y="{pad_t}" width="{pw}" height="{ph}" fill="none" stroke="{GRID}" stroke-width="1"/>')
    # median crosshair
    p.append(f'<line x1="{mx:.1f}" y1="{pad_t}" x2="{mx:.1f}" y2="{pad_t+ph}" stroke="{NAVY_SOFT}" stroke-width="1" stroke-dasharray="3 3" opacity="0.5"/>')
    p.append(f'<line x1="{pad_l}" y1="{my:.1f}" x2="{pad_l+pw}" y2="{my:.1f}" stroke="{NAVY_SOFT}" stroke-width="1" stroke-dasharray="3 3" opacity="0.5"/>')

    # quadrant labels
    q = quadrants or {}
    def qlabel(x, y, anchor, text):
        if not text:
            return
        p.append(
            f'<text x="{x:.0f}" y="{y:.0f}" text-anchor="{anchor}" font-size="10.5" '
            f'font-weight="700" letter-spacing="1" fill="{MUTE}" '
            f'font-family="{_FONT}" opacity="0.8">{escape(text)}</text>'
        )
    qlabel(pad_l + pw - 6, pad_t + 14, "end", q.get("tr", ""))
    qlabel(pad_l + 6, pad_t + 14, "start", q.get("tl", ""))
    qlabel(pad_l + pw - 6, pad_t + ph - 8, "end", q.get("br", ""))
    qlabel(pad_l + 6, pad_t + ph - 8, "start", q.get("bl", ""))

    # axis titles
    p.append(f'<text x="{pad_l+pw/2:.0f}" y="{height-14}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{NAVY}" font-family="{_FONT}">{escape(x_title)}</text>')
    p.append(f'<text x="16" y="{pad_t+ph/2:.0f}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{NAVY}" font-family="{_FONT}" transform="rotate(-90 16 {pad_t+ph/2:.0f})">{escape(y_title)}</text>')
    # axis scale ticks (lo / mid / hi), inverse-mapped to data units
    for frac in (0.0, 0.5, 1.0):
        yv = ylo + (yhi - ylo) * frac
        p.append(f'<text x="{pad_l-8}" y="{py(yv)+3:.1f}" text-anchor="end" font-size="9" fill="{MUTE}" font-family="{_FONT}">{_fmt(yv)}</text>')
        xv = xlo + (xhi - xlo) * frac
        p.append(f'<text x="{px(xv):.1f}" y="{pad_t+ph+15}" text-anchor="middle" font-size="9" fill="{MUTE}" font-family="{_FONT}">{_fmt(xv)}</text>')

    # bubbles, largest first so small ones stay on top
    order = sorted(range(len(items)), key=lambda i: sizes[i], reverse=True)
    for i in order:
        it = items[i]
        x, y, r = px(xs[i]), py(ys[i]), radius(sizes[i])
        hot = it.get("highlight")
        fill = CYAN if hot else NAVY
        p.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{fill}" opacity="{0.85 if hot else 0.62}" stroke="#fff" stroke-width="1.5"/>')
        lx, anchor = x + r + 5, "start"
        if lx > pad_l + pw + pad_r - 30:  # near right edge → flip left
            lx, anchor = x - r - 5, "end"
        p.append(
            f'<text x="{lx:.1f}" y="{y+3:.1f}" text-anchor="{anchor}" font-size="10.5" '
            f'font-weight="{700 if hot else 600}" fill="{INK}" font-family="{_FONT}">'
            f'{escape(_first_name(it["label"]))}</text>'
        )
    return _svg(width, height, "".join(p))


def quality_matrix(items: list[dict], *, width: int = 680, height: int = 520) -> str:
    """The hero exhibit: output (x, log) vs model-judged quality (y), bubble = churn.

    Thin wrapper over scatter(). items: [{label, output, quality, churn, highlight?}].
    Quadrants — Stars / Craftspeople / Workhorses / Watch.
    """
    return scatter(
        [
            {
                "x": max(0, it["output"]),
                "y": max(0, min(100, it["quality"])),
                "size": it.get("churn", 1),
                "label": it["label"],
                "highlight": it.get("highlight"),
            }
            for it in items
        ],
        x_title="Output  (commits, log scale) →",
        y_title="Model-judged quality →",
        x_scale="log",
        y_zoom=True,
        y_clamp=(0, 100),
        quadrants={"tr": "STARS", "tl": "CRAFTSPEOPLE", "br": "WORKHORSES", "bl": "WATCH"},
        width=width,
        height=height,
    )


def _first_name(name: str) -> str:
    parts = name.split()
    return name if len(name) <= 16 else (parts[0] if parts else name)[:16]


def race_radar(label: str, values: dict, *, size: int = 184, highlight: bool = False) -> str:
    """A single contributor's RACE quality fingerprint (4-axis radar)."""
    axes = [
        ("Readability", values.get("readability", 0)),
        ("Maintainability", values.get("maintainability", 0)),
        ("Correctness", values.get("correctness", 0)),
        ("Efficiency", values.get("efficiency", 0)),
    ]
    cx = cy = size / 2
    R = size / 2 - 30
    import math

    # 4 axes at top/right/bottom/left
    angles = [-90, 0, 90, 180]
    grid = []
    for ring in (0.25, 0.5, 0.75, 1.0):
        pts = []
        for a in angles:
            rad = math.radians(a)
            pts.append(f"{cx + R*ring*math.cos(rad):.1f},{cy + R*ring*math.sin(rad):.1f}")
        grid.append(f'<polygon points="{" ".join(pts)}" fill="none" stroke="{GRID}" stroke-width="1"/>')
    spokes = []
    poly = []
    labels = []
    for (name, val), a in zip(axes, angles):
        rad = math.radians(a)
        ex, ey = cx + R*math.cos(rad), cy + R*math.sin(rad)
        spokes.append(f'<line x1="{cx:.1f}" y1="{cy:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="{GRID}" stroke-width="1"/>')
        vr = R * max(0, min(100, val)) / 100
        poly.append(f"{cx + vr*math.cos(rad):.1f},{cy + vr*math.sin(rad):.1f}")
        # axis letter + value
        lx, ly = cx + (R+14)*math.cos(rad), cy + (R+14)*math.sin(rad)
        anchor = "middle" if a in (-90, 90) else ("start" if a == 0 else "end")
        labels.append(
            f'<text x="{lx:.1f}" y="{ly+3:.1f}" text-anchor="{anchor}" font-size="8.5" '
            f'fill="{MUTE}" font-family="{_FONT}">{name[0]}</text>'
        )
    color = CYAN if highlight else NAVY
    body = (
        "".join(grid) + "".join(spokes)
        + f'<polygon points="{" ".join(poly)}" fill="{color}" fill-opacity="0.22" stroke="{color}" stroke-width="2"/>'
        + "".join(
            f'<circle cx="{pt.split(",")[0]}" cy="{pt.split(",")[1]}" r="2.4" fill="{color}"/>'
            for pt in poly
        )
        + "".join(labels)
        + f'<text x="{cx:.0f}" y="{size-6}" text-anchor="middle" font-size="11" '
          f'font-weight="700" fill="{NAVY}" font-family="{_FONT}">{escape(_first_name(label))}</text>'
    )
    return _svg(size, size, body)


def _legend(entries: list[tuple[str, str]], width: int) -> str:
    chips, x = [], 8
    for text, color in entries:
        chips.append(
            f'<rect x="{x}" y="3" width="11" height="11" fill="{color}" rx="1"/>'
            f'<text x="{x + 16}" y="12.5" font-size="10.5" fill="{MUTE}" '
            f'font-family="{_FONT}">{escape(text)}</text>'
        )
        x += 22 + len(text) * 7
    return _svg(width, 20, "".join(chips))


def _svg(width: int, height: int, body: str) -> str:
    return (
        f'<svg viewBox="0 0 {width} {height}" width="100%" '
        f'preserveAspectRatio="xMinYMin meet" role="img" '
        f'xmlns="http://www.w3.org/2000/svg" style="max-width:{width}px">{body}</svg>'
    )


def _empty(width: int, height: int) -> str:
    return _svg(
        width,
        height,
        f'<text x="{width / 2}" y="{height / 2}" text-anchor="middle" '
        f'font-size="12" fill="{MUTE}" font-family="{_FONT}">No data</text>',
    )
