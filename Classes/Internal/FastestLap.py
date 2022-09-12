from pydantic import BaseModel
from Classes.Internal.Time import Time
from Classes.Internal.AverageSpeed import AverageSpeed


class FastestLap(BaseModel):
    rank: int
    lap: int
    Time: Time
    AverageSpeed: AverageSpeed
