from pydantic_settings import BaseSettings
from typing import Optional
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv(".env", override=True)


class EnvSettings(BaseSettings):

    # Neo4j settings
    NEO4J_URI: str = os.getenv("NEO4J_URI")
    NEO4J_USERNAME: str = os.getenv("NEO4J_USERNAME") 
    NEO4J_PASSWORD: str = os.getenv("NEO4J_PASSWORD")
    AURA_INSTANCEID: str = os.getenv("AURA_INSTANCEID")
    AURA_INSTANCENAME: str = os.getenv("AURA_INSTANCENAME")

    # OpenAI settings
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")

    # LangChain settings
    LANGCHAIN_TRACING_V2: str = os.getenv("LANGCHAIN_TRACING_V2")
    LANGCHAIN_ENDPOINT: str = os.getenv("LANGCHAIN_ENDPOINT")
    LANGCHAIN_API_KEY: str = os.getenv("LANGCHAIN_API_KEY")
    LANGCHAIN_PROJECT: str = os.getenv("LANGCHAIN_PROJECT")

    # Optional API settings
    API_HOST: str = os.getenv("API_HOST", "localhost")
    API_PORT: int = int(os.getenv("API_PORT", "8000"))

    class Config:
        env_file = ".env"
        case_sensitive = True


# Create settings instance
settings = EnvSettings()
