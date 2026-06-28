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
