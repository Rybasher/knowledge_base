from fastapi import APIRouter

router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": ""}, {"username": ""}]


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}
