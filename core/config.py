from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
class Settings(BaseSettings):
    db_url : str = f"sqlite+aiosqlite:///./db.sqlite3"
    db_echo : bool = True #False

settings = Settings()