from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import Dict
from rag.route import router as rag_router
from configs.env_config import settings

# Initialize FastAPI app
app = FastAPI(
    title="FastAPI Service", description="Simple FastAPI service", version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include RAG router
app.include_router(rag_router)

# Health check endpoint
@app.get("/health")
async def health_check() -> Dict[str, str]:
    return {"status": "healthy", "version": app.version}


if __name__ == "__main__":
    import uvicorn
    
    # Validate settings on startup
    assert settings.NEO4J_URI, "NEO4J_URI must be set"
    assert settings.NEO4J_USERNAME, "NEO4J_USERNAME must be set"
    assert settings.NEO4J_PASSWORD, "NEO4J_PASSWORD must be set"
    assert settings.AURA_INSTANCEID, "AURA_INSTANCEID must be set"
    assert settings.AURA_INSTANCENAME, "AURA_INSTANCENAME must be set"
    assert settings.OPENAI_API_KEY, "OPENAI_API_KEY must be set"
    assert settings.LANGCHAIN_TRACING_V2, "LANGCHAIN_TRACING_V2 must be set"
    assert settings.LANGCHAIN_ENDPOINT, "LANGCHAIN_ENDPOINT must be set"
    assert settings.LANGCHAIN_API_KEY, "LANGCHAIN_API_KEY must be set"
    assert settings.LANGCHAIN_PROJECT, "LANGCHAIN_PROJECT must be set"
    assert settings.API_HOST, "API_HOST must be set"
    assert settings.API_PORT, "API_PORT must be set"

    uvicorn.run("app:app", host=settings.API_HOST, port=settings.API_PORT)
