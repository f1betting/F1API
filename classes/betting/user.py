import uuid

from pydantic import BaseModel


class BaseUser(BaseModel):
    first_name: str
    last_name: str


class FullUser(BaseUser):
    uuid: str


class Users(list[FullUser]):
    pass


UserExample = {
    "first_name": "Niek",
    "last_name": "Verstappen",
    "id": uuid.uuid4()
}
