import pydantic_settings


class DBCredentials(pydantic_settings.BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str

    @property
    def URL(self) -> str:
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    model_config = pydantic_settings.SettingsConfigDict(
        env_file='settings.env')


db_credentials = DBCredentials()  # type: ignore
