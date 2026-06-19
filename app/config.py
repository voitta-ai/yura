"""Application configuration and resolved filesystem paths."""
from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# Project root = parent of the `app` package.
ROOT_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="YURA_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    host: str = "127.0.0.1"
    port: int = 8000

    # Storage locations (relative paths resolved against ROOT_DIR).
    data_dir: Path = Path("./data")
    workspace_dir: Path = Path("./workspace")

    @property
    def data_path(self) -> Path:
        p = self.data_dir if self.data_dir.is_absolute() else ROOT_DIR / self.data_dir
        p.mkdir(parents=True, exist_ok=True)
        return p

    @property
    def workspace_path(self) -> Path:
        p = (
            self.workspace_dir
            if self.workspace_dir.is_absolute()
            else ROOT_DIR / self.workspace_dir
        )
        p.mkdir(parents=True, exist_ok=True)
        return p

    @property
    def db_path(self) -> Path:
        return self.data_path / "yura.sqlite"

    @property
    def db_url(self) -> str:
        return f"sqlite:///{self.db_path}"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
