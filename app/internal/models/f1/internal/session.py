from pydantic import BaseModel


class Session(BaseModel):
    date: str | None
    time: str | None
