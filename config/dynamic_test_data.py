from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class DynamicTestData(BaseSettings, extra="ignore"):
    """A settings class for dynamic test data using pydantic.

    This class loads configuration from environment variables.
    """

    app_url: str = Field()
    email_login: str = Field()
    email_password: SecretStr = Field()
    contant_name: str = "demo_bdd"

    model_config = SettingsConfigDict(
        env_prefix="demo_bdd_",
        env_file=".env",
        case_sensitive=False,
    )
