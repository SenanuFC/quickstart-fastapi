from fastapi import APIRouter

router = APIRouter(prefix='/users')

@router.post("/")
async def add_user():
    return {}
