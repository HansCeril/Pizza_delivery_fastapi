from fastapi import APIRouter

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@auth_router.get('/auth')
async def hello():
    return {"messages": "Hello world"}