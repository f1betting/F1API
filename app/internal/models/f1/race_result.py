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
    "timestamp": 1669983525.3542814,
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
        },
        {
            "timestamp": None,
            "number": 16,
            "position": 2,
            "positionText": "2",
            "points": 18,
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
            "Constructor": {
                "timestamp": None,
                "constructorId": "ferrari",
                "url": "https://en.wikipedia.org/wiki/Scuderia_Ferrari",
                "name": "Ferrari",
                "nationality": "Italian"
            },
            "grid": 3,
            "laps": 58,
            "status": "Finished",
            "Time": {
                "time": "+8.771",
                "millis": "5274685"
            },
            "FastestLap": {
                "rank": 10,
                "lap": 48,
                "Time": {
                    "time": "1:29.719",
                    "millis": None
                },
                "AverageSpeed": {
                    "units": "kph",
                    "speed": 211.901
                }
            }
        },
        {
            "timestamp": None,
            "number": 11,
            "position": 3,
            "positionText": "3",
            "points": 15,
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
            "Constructor": {
                "timestamp": None,
                "constructorId": "red_bull",
                "url": "https://en.wikipedia.org/wiki/Red_Bull_Racing",
                "name": "Red Bull",
                "nationality": "Austrian"
            },
            "grid": 2,
            "laps": 58,
            "status": "Finished",
            "Time": {
                "time": "+10.093",
                "millis": "5276007"
            },
            "FastestLap": {
                "rank": 4,
                "lap": 52,
                "Time": {
                    "time": "1:28.972",
                    "millis": None
                },
                "AverageSpeed": {
                    "units": "kph",
                    "speed": 213.68
                }
            }
        },
        {
            "timestamp": None,
            "number": 55,
            "position": 4,
            "positionText": "4",
            "points": 12,
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
            "Constructor": {
                "timestamp": None,
                "constructorId": "ferrari",
                "url": "https://en.wikipedia.org/wiki/Scuderia_Ferrari",
                "name": "Ferrari",
                "nationality": "Italian"
            },
            "grid": 4,
            "laps": 58,
            "status": "Finished",
            "Time": {
                "time": "+24.892",
                "millis": "5290806"
            },
            "FastestLap": {
                "rank": 3,
                "lap": 50,
                "Time": {
                    "time": "1:28.879",
                    "millis": None
                },
                "AverageSpeed": {
                    "units": "kph",
                    "speed": 213.904
                }
            }
        },
        {
            "timestamp": None,
            "number": 63,
            "position": 5,
            "positionText": "5",
            "points": 10,
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
            "Constructor": {
                "timestamp": None,
                "constructorId": "mercedes",
                "url": "https://en.wikipedia.org/wiki/Mercedes-Benz_in_Formula_One",
                "name": "Mercedes",
                "nationality": "German"
            },
            "grid": 6,
            "laps": 58,
            "status": "Finished",
            "Time": {
                "time": "+35.888",
                "millis": "5301802"
            },
            "FastestLap": {
                "rank": 2,
                "lap": 48,
                "Time": {
                    "time": "1:28.836",
                    "millis": None
                },
                "AverageSpeed": {
                    "units": "kph",
                    "speed": 214.007
                }
            }
        },
        {
            "timestamp": None,
            "number": 4,
            "position": 6,
            "positionText": "6",
            "points": 9,
            "Driver": {
                "timestamp": None,
                "driverId": "norris",
                "url": "https://en.wikipedia.org/wiki/Lando_Norris",
                "givenName": "Lando",
                "familyName": "Norris",
                "dateOfBirth": "1999-11-13",
                "nationality": "British",
                "permanentNumber": 4,
                "code": "NOR"
            },
            "Constructor": {
                "timestamp": None,
                "constructorId": "mclaren",
                "url": "https://en.wikipedia.org/wiki/McLaren",
                "name": "McLaren",
                "nationality": "British"
            },
            "grid": 7,
            "laps": 58,
            "status": "Finished",
            "Time": {
                "time": "+56.234",
                "millis": "5322148"
            },
            "FastestLap": {
                "rank": 1,
                "lap": 44,
                "Time": {
                    "time": "1:28.391",
                    "millis": None
                },
                "AverageSpeed": {
                    "units": "kph",
                    "speed": 215.085
                }
            }
        }
    ]
}
