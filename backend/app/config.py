from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_NAME: str = "PDF AI Backend"
    FRONTEND_ORIGIN: str = "http://localhost:3000"

settings = Settings()
