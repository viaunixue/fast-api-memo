from pydantic import (
    BaseSettings, 
    SettingsConfigDict,
    MySQLDsn,
    computed_field
)

from pydantic_core import MultiHostUrl

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_ignore_empty=True, extra="ignore"
    )

    API_V1_STR: str

    PROJECT_NAME : str

    MYSQL_USER : str
    MYSQL_PASSWORD : str
    MYSQL_SERVER : str
    MYSQL_PORT : int
    MYSQL_DB : str

    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> MySQLDsn:
        return MultiHostUrl.build(
            scheme="mysql+pymysql",
            username=self.MYSQL_USER,
            password=self.MYSQL_PASSWORD,
            host=self.MYSQL_SERVER,
            port=self.MYSQL_PORT,
            path=self.MYSQL_DB,
        )

settings = Settings()

