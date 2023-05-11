from pydantic import BaseSettings, validator


class Settings(BaseSettings):

    API_V1_STR: str = "/api/v1"
    APP_NAME: str
    DOMAIN: str
    DEBUG_MODE: bool = True
    BACKEND_PORT: int

    @validator("BACKEND_PORT", pre=True)
    def SetPortDefault(cls, v: str):
        if v:
            return v
        return 8000

settings = Settings()
