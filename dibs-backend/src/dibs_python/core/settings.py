from functools import lru_cache

from pydantic import SecretStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Class containing 'Dibs' app settings. Used in
    most of the instances in codebase
    """

    # app settings
    app_debug: bool = True
    app_version: str = "0.0.1"

    # db settings
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: SecretStr

    @property
    def db_url(self) -> str:
        """
        Function to get database url from settings
        """
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password.get_secret_value()}@{self.db_host}:{self.db_port}/{self.db_name}"

    # uvicorn deployment settings
    uvicorn_host: str
    uvicorn_port: int

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }


@lru_cache
def get_settings() -> Settings:
    """
    Function to get 'Dibs' app settings. Used in
    most of the instances in codebase
    """
    return Settings()  # type: ignore
