from pydantic import BaseModel


class AverageSpeed(BaseModel):
    units: str
    speed: float

