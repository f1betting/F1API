import uuid

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

import main
from classes.betting.user import UserExample, BaseUser, FullUser, Users
from classes.general.message import Message, create_message

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/",
            response_model=Users,
            responses={
                404: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Users not found")
                    }
                }},
                200: {"model": Users, "content": {
                    "application/json": {
                        "example": [
                            UserExample
                        ]
                    }
                }}
            })
def get_all_users():
    users = list(main.app.database["Users"].find())

    if not users:
        return JSONResponse(status_code=404, content=create_message("Users not found"))

    for user in users:
        del user["_id"]

    return users


@router.get("/{username}",
            response_model=FullUser,
            responses={
                404: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("User not found")
                    }
                }},
                200: {"model": FullUser, "content": {
                    "application/json": {
                        "example": UserExample
                    }
                }}
            })
def get_user_by_username(username: str):
    user = main.app.database["Users"].find_one({"username": username})

    if not user:
        return JSONResponse(status_code=404, content=create_message("User not found"))

    return user


@router.post("/",
             response_model=FullUser,
             responses={
                 409: {"model": Message, "content": {
                     "application/json": {
                         "example": create_message("User already exists")
                     }
                 }},
                 200: {"model": FullUser, "content": {
                     "application/json": {
                         "example": UserExample
                     }
                 }}
             })
def create_user(user: BaseUser):
    user.username = user.username.lower()

    user = jsonable_encoder(user)

    user["points"] = 0
    user["uuid"] = str(uuid.uuid4())

    if list(main.app.database["Users"].find({"username": user["username"]})):
        return JSONResponse(status_code=409, content=create_message("User already exists"))

    new_user = main.app.database["Users"].insert_one(user)

    created_user = main.app.database["Users"].find_one({"_id": new_user.inserted_id})

    return created_user
