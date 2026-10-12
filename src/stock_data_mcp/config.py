"""Settings loaded from the environment and the repo-level .env file."""

from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# Claude Desktop launches the server from an arbitrary cwd, so resolve .env
# relative to the repository instead of the working directory.
REPO_ROOT = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=REPO_ROOT / ".env", env_file_encoding="utf-8", extra="ignore")

    # SEC requires a descriptive User-Agent: "Name email@example.com".
    sec_user_agent: str = Field(min_length=5)
    fred_api_key: str | None = None
    cache_path: Path = REPO_ROOT / ".cache" / "stock_data.sqlite"
    edgar_max_rps: float = 8.0
    log_level: str = "INFO"


@lru_cache
def get_settings() -> Settings:
    return Settings()  # type: ignore[call-arg]
