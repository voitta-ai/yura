"""Repository lifecycle: add → choose branch → clone (full history)."""
from __future__ import annotations

import shutil

from fastapi import APIRouter, BackgroundTasks, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session

from app.config import settings
from app.db import SessionLocal, get_db
from app.models import Repository
from app.services import git_service
from app.services import models_service
from app.services import settings_store as store
from app.templating import templates

router = APIRouter(tags=["repos"])


@router.get("/", response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    repos = db.query(Repository).order_by(Repository.created_at.desc()).all()
    return templates.TemplateResponse(
        "index.html", {"request": request, "repos": repos}
    )


@router.post("/repos/branches", response_class=HTMLResponse)
def choose_branch(request: Request, url: str = Form(...)):
    url = url.strip()
    error, branches = None, []
    try:
        branches = git_service.list_remote_branches(url)
        if not branches:
            error = "No branches found at that URL."
    except git_service.GitError as exc:
        error = str(exc)
    return templates.TemplateResponse(
        "branches.html",
        {
            "request": request,
            "url": url,
            "name": git_service.derive_repo_name(url),
            "branches": branches,
            "error": error,
        },
    )


@router.post("/repos")
def create_repo(
    background: BackgroundTasks,
    db: Session = Depends(get_db),
    url: str = Form(...),
    branch: str = Form(...),
    name: str = Form(...),
):
    repo = Repository(
        url=url.strip(),
        name=name.strip() or git_service.derive_repo_name(url),
        branch=branch,
        clone_status="cloning",
    )
    db.add(repo)
    db.commit()
    db.refresh(repo)
    background.add_task(_clone_task, repo.id)
    return RedirectResponse(url=f"/repos/{repo.id}", status_code=303)


@router.get("/repos/{repo_id}", response_class=HTMLResponse)
def repo_detail(repo_id: int, request: Request, db: Session = Depends(get_db)):
    repo = db.get(Repository, repo_id)
    if repo is None:
        return RedirectResponse(url="/", status_code=303)
    values = store.get_all(db)
    cap = int(values.get("max_commits_per_run") or 300)
    # Per-provider model lists for the on-page model/provider picker (lets the
    # user experiment with cost projections without touching global Settings).
    anthropic_models, _ = models_service.list_models(
        "anthropic", values["anthropic_api_key"], current=values["anthropic_model"]
    )
    openai_models, _ = models_service.list_models(
        "openai", values["openai_api_key"], current=values["openai_model"]
    )
    return templates.TemplateResponse(
        "repo.html",
        {
            "request": request,
            "repo": repo,
            "runs": repo.runs,
            "cap": cap,
            "provider": values["llm_provider"],
            "anthropic_model": values["anthropic_model"],
            "openai_model": values["openai_model"],
            "anthropic_models": anthropic_models,
            "openai_models": openai_models,
        },
    )


@router.post("/repos/{repo_id}/delete")
def delete_repo(repo_id: int, db: Session = Depends(get_db)):
    repo = db.get(Repository, repo_id)
    if repo is not None:
        if repo.local_path:
            shutil.rmtree(repo.local_path, ignore_errors=True)
        db.delete(repo)
        db.commit()
    return RedirectResponse(url="/", status_code=303)


def _clone_task(repo_id: int) -> None:
    """Background: full clone of the chosen branch; update status on the row."""
    db = SessionLocal()
    try:
        repo = db.get(Repository, repo_id)
        if repo is None:
            return
        dest = settings.workspace_path / f"repo-{repo.id}"
        try:
            git_service.clone_repo(repo.url, repo.branch, dest)
            repo.local_path = str(dest)
            repo.clone_status = "ready"
            repo.clone_message = ""
        except git_service.GitError as exc:
            repo.clone_status = "error"
            repo.clone_message = str(exc)
        db.commit()
    finally:
        db.close()
