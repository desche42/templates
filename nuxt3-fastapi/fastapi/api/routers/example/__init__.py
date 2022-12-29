"""
Subrouter example
"""
from fastapi import APIRouter
from .subroute import router as subroute_router
router = APIRouter()

@router.get(
    "/"
)
async def example_router():
    "Example subroute"
    return "This is an example route"


router.include_router(
    subroute_router, prefix="/subrouter-prefix"
)
