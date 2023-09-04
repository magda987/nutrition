from pydantic import SecretStr, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

postgres_host: str = "localhost"
postgress_port: str = "5432"
postgres_user: str = "postgres"
postgres_password: SecretStr = SecretStr("postgres")
postgres_db: str = "postgres"
    
@property
def daabase_uri(self)  -> PostgresDsn:
    return (
        f"postgresql+psycopg://"
        f"{self.postgres_user}:self.postgres_password.get_secret_value()"
        f"@{self.postgres_host}:{self.postgres_port}"
        f"/{self.postgres_db}"
    )


settings = Settings()