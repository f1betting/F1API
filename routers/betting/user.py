import uuid

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

import main
from classes.betting.user import UserExample, BaseUser, FullUser, Users
from classes.general.message import Message

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/",
            response_model=Users,
            responses={
                404: {"model": Message, "description": "Users not found"},
                200: {"model": Users, "content": {
                    "application/json": {
                        "example": [
                            UserExample
                        ]
                    }
                }}
            }
            )
def get_all_users():
    users = list(main.app.database["Users"].find())

    if not users:
        return JSONResponse(status_code=404, content={"message": "Users not found"})

    for user in users:
        del user["_id"]

    return users


@router.get("/{user_uuid}",
            response_model=FullUser,
            responses={
                404: {"model": Message, "description": "User not found"},
                200: {"model": FullUser, "content": {
                    "application/json": {
                        "example": UserExample
                    }
                }}
            })
def get_user_by_uuid(user_uuid: str):
    user = main.app.database["Users"].find_one({"uuid": user_uuid})

    if not user:
        return JSONResponse(status_code=404, content={"message": "User not found"})

    return user


@router.post("/",
             response_model=FullUser,
             responses={
                 200: {"model": FullUser, "content": {
                     "application/json": {
                         "example": UserExample
                     }
                 }}
             })
def create_user(user: BaseUser):
    user.first_name = user.first_name.lower()
    user.last_name = user.last_name.lower()

    user = jsonable_encoder(user)

    user["uuid"] = str(uuid.uuid4())

    new_user = main.app.database["Users"].insert_one(user)

    created_user = main.app.database["Users"].find_one({"_id": new_user.inserted_id})

    return created_user
