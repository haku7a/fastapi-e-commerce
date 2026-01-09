from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str
    API_V1_STR: str = "/api/v1"

    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)


settings = Settings()
