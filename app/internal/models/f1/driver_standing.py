from pydantic import BaseModel
from app.internal.models.f1.constructor import Constructor
from app.internal.models.f1.driver import Driver


class DriverStanding(BaseModel):
    position: int
    positionText: str
    points: int
    wins: int
    Driver: Driver
    Constructors: list[Constructor]


class DriverStandings(BaseModel):
    standings: list[DriverStanding]


DriverStandingsExample = {
    "position": 1,
    "positionText": "1",
    "points": 335,
    "wins": 11,
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
    "Constructors": [
        {
            "constructorId": "red_bull",
            "url": "http://en.wikipedia.org/wiki/Red_Bull_Racing",
            "name": "Red Bull",
            "nationality": "Austrian"
        }
    ]
}
