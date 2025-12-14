from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()


@dataclass
class Settings:
	PROJECT_NAME: str = os.getenv("PROJECT_NAME", "UniMarket")
	VERSION: str = os.getenv("VERSION", "0.1.0")
	DEBUG: bool = os.getenv("DEBUG", "True").lower() in ("1", "true", "yes")
	API_PREFIX: str = os.getenv("API_PREFIX", "/api/v1")
	AUTHOR: str = os.getenv("AUTHOR", "Студент курса FastAPI")


settings = Settings()
