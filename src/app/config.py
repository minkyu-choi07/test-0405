"""App configuration via pydantic-settings."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="APP_",
    )

    app_name: str = "My Streamlit App"
    debug: bool = False
    api_base_url: str = "https://api.example.com"
    database_url: str = "sqlite:///data.db"
    cache_ttl_seconds: int = 300


# Singleton — import this everywhere
settings = Settings()
