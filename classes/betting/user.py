import uuid

from pydantic import BaseModel


class BaseUser(BaseModel):
    username: str


class FullUser(BaseUser):
    uuid: str
    points: int


class Users(list[FullUser]):
    pass


UserExample = {
    "username": "Niek",
    "uuid": uuid.uuid4(),
    "points": 0
}

UserCreateExample = {
    "username": "Niek",
}
