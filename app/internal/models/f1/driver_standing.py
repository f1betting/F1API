from app.internal.models.f1.constructor import Constructor
from app.internal.models.f1.driver import Driver
from app.internal.models.general.request import BaseRequest


class DriverStanding(BaseRequest):
    position: int
    positionText: str
    points: int
    wins: int
    Driver: Driver
    Constructors: list[Constructor]


class DriverStandings(BaseRequest):
    standings: list[DriverStanding]


# pylint: disable=duplicate-code
DriverStandingsExample = {
    "timestamp": 1669977611.5538518,
    "standings": [
        {
            "timestamp": None,
            "position": 1,
            "positionText": "1",
            "points": 454,
            "wins": 15,
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
            "Constructors": [
                {
                    "timestamp": None,
                    "constructorId": "red_bull",
                    "url": "https://en.wikipedia.org/wiki/Red_Bull_Racing",
                    "name": "Red Bull",
                    "nationality": "Austrian"
                }
            ]
        }
    ]
}
