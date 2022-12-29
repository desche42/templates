"""
Subrouter example
"""
from fastapi import APIRouter


router = APIRouter()

@router.get(
    "/route"
)
async def example_router():
    "Example subroute"
    return "This is a subroute"
