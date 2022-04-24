from pydantic import BaseSettings


class Setting(BaseSettings):
    app_name: str = "test"
    database_url: str

    class Config:
        env_file = ".env"
