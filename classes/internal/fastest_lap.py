from pydantic import BaseModel
from classes.internal.time import Time
from classes.internal.average_speed import AverageSpeed


class FastestLap(BaseModel):
    rank: int
    lap: int
    Time: Time
    AverageSpeed: AverageSpeed
