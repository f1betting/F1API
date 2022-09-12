from pydantic import BaseModel


class Time(BaseModel):
    time: str
    millis: str | None
