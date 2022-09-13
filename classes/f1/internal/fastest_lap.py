from pydantic import BaseModel
from classes.f1.internal.time import Time
from classes.f1.internal.average_speed import AverageSpeed


class FastestLap(BaseModel):
    rank: int
    lap: int
    Time: Time
    AverageSpeed: AverageSpeed
