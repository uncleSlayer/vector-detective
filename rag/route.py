from fastapi.routing import APIRouter

router = APIRouter()

@router.get("/rag/ask")
async def dummy_route():
    """A simple dummy route for testing"""
    return {"message": "This is a dummy route"}
