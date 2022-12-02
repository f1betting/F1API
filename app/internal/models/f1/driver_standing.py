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
    "timestamp": 1669984278.61889,
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
        },
        {
            "timestamp": None,
            "position": 2,
            "positionText": "2",
            "points": 308,
            "wins": 3,
            "Driver": {
                "timestamp": None,
                "driverId": "leclerc",
                "url": "https://en.wikipedia.org/wiki/Charles_Leclerc",
                "givenName": "Charles",
                "familyName": "Leclerc",
                "dateOfBirth": "1997-10-16",
                "nationality": "Monegasque",
                "permanentNumber": 16,
                "code": "LEC"
            },
            "Constructors": [
                {
                    "timestamp": None,
                    "constructorId": "ferrari",
                    "url": "https://en.wikipedia.org/wiki/Scuderia_Ferrari",
                    "name": "Ferrari",
                    "nationality": "Italian"
                }
            ]
        },
        {
            "timestamp": None,
            "position": 3,
            "positionText": "3",
            "points": 305,
            "wins": 2,
            "Driver": {
                "timestamp": None,
                "driverId": "perez",
                "url": "https://en.wikipedia.org/wiki/Sergio_P%C3%A9rez",
                "givenName": "Sergio",
                "familyName": "Pérez",
                "dateOfBirth": "1990-01-26",
                "nationality": "Mexican",
                "permanentNumber": 11,
                "code": "PER"
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
        },
        {
            "timestamp": None,
            "position": 4,
            "positionText": "4",
            "points": 275,
            "wins": 1,
            "Driver": {
                "timestamp": None,
                "driverId": "russell",
                "url": "https://en.wikipedia.org/wiki/George_Russell_%28racing_driver%29",
                "givenName": "George",
                "familyName": "Russell",
                "dateOfBirth": "1998-02-15",
                "nationality": "British",
                "permanentNumber": 63,
                "code": "RUS"
            },
            "Constructors": [
                {
                    "timestamp": None,
                    "constructorId": "mercedes",
                    "url": "https://en.wikipedia.org/wiki/Mercedes-Benz_in_Formula_One",
                    "name": "Mercedes",
                    "nationality": "German"
                }
            ]
        },
        {
            "timestamp": None,
            "position": 5,
            "positionText": "5",
            "points": 246,
            "wins": 1,
            "Driver": {
                "timestamp": None,
                "driverId": "sainz",
                "url": "https://en.wikipedia.org/wiki/Carlos_Sainz_Jr.",
                "givenName": "Carlos",
                "familyName": "Sainz",
                "dateOfBirth": "1994-09-01",
                "nationality": "Spanish",
                "permanentNumber": 55,
                "code": "SAI"
            },
            "Constructors": [
                {
                    "timestamp": None,
                    "constructorId": "ferrari",
                    "url": "https://en.wikipedia.org/wiki/Scuderia_Ferrari",
                    "name": "Ferrari",
                    "nationality": "Italian"
                }
            ]
        }
    ]
}
