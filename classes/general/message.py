from pydantic import BaseModel


class Message(BaseModel):
    message: str


def create_message(msg: str):
    return {
        "message": f"{msg}"
    }
