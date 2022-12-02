from app.internal.models.f1.constructor import Constructor
from app.internal.models.f1.driver import Driver
from app.internal.models.f1.internal.fastest_lap import FastestLap
from app.internal.models.f1.internal.time import Time
from app.internal.models.general.request import BaseRequest


class RaceResult(BaseRequest):
    number: int
    position: int
    positionText: str
    points: float
    Driver: Driver
    Constructor: Constructor
    grid: int
    laps: int
    status: str
    Time: Time | None
    FastestLap: FastestLap | None


class RaceResults(BaseRequest):
    results: list[RaceResult]


# pylint: disable=duplicate-code
RaceResultExample = {
    "timestamp": 1669978263.7017405,
    "results": [
        {
            "timestamp": None,
            "number": 1,
            "position": 1,
            "positionText": "1",
            "points": 25,
            "Driver": {
                "timestamp": None,
                "driverId": "max_verstappen",
                "url": "https://en.wikipedia.org/wiki/Max_Verstappen",
                "givenName": "Max",
                "familyName": "Verstappen",
                "dateOfBirth": "1997-09-30",
                "nationality": "Dutch",
                "permanentNumber": 33,
                "code": "VER"
            },
            "Constructor": {
                "timestamp": None,
                "constructorId": "red_bull",
                "url": "https://en.wikipedia.org/wiki/Red_Bull_Racing",
                "name": "Red Bull",
                "nationality": "Austrian"
            },
            "grid": 1,
            "laps": 58,
            "status": "Finished",
            "Time": {
                "time": "1:27:45.914",
                "millis": "5265914"
            },
            "FastestLap": {
                "rank": 6,
                "lap": 54,
                "Time": {
                    "time": "1:29.392",
                    "millis": None
                },
                "AverageSpeed": {
                    "units": "kph",
                    "speed": 212.676
                }
            }
        }
    ]
}
