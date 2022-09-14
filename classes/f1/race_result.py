from pydantic import BaseModel

from classes.f1.constructor import Constructor
from classes.f1.driver import Driver
from classes.f1.internal.fastest_lap import FastestLap
from classes.f1.internal.time import Time


class RaceResult(BaseModel):
    number: int
    position: int
    positionText: str
    points: int
    Driver: Driver
    Constructor: Constructor
    grid: int
    laps: int
    status: str
    Time: Time | None
    FastestLap: FastestLap | None


class RaceResults(BaseModel):
    results: list[RaceResult]


RaceResultExample = {
    "number": 1,
    "position": 1,
    "positionText": "1",
    "points": 26,
    "Driver": {
        "driverId": "max_verstappen",
        "url": "http://en.wikipedia.org/wiki/Max_Verstappen",
        "givenName": "Max",
        "familyName": "Verstappen",
        "dateOfBirth": "1997-09-30",
        "nationality": "Dutch",
        "permanentNumber": 33,
        "code": "VER"
    },
    "Constructor": {
        "constructorId": "red_bull",
        "url": "http://en.wikipedia.org/wiki/Red_Bull_Racing",
        "name": "Red Bull",
        "nationality": "Austrian"
    },
    "grid": 1,
    "laps": 72,
    "status": "Finished",
    "Time": {
        "time": "1:36:42.773",
        "millis": "5802773"
    },
    "FastestLap": {
        "rank": 1,
        "lap": 62,
        "Time": {
            "time": "1:13.652",
            "millis": None
        },
        "AverageSpeed": {
            "units": "kph",
            "speed": 208.173
        }
    }
}
