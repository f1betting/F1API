from app.internal.models.f1.constructor import Constructor
from app.internal.models.f1.driver import Driver
from app.internal.models.general.request import BaseRequest


class QualifyingResult(BaseRequest):
    number: int
    position: int
    Driver: Driver
    Constructor: Constructor
    Q1: str | None
    Q2: str | None
    Q3: str | None


class QualifyingResults(BaseRequest):
    results: list[QualifyingResult]


# pylint: disable=duplicate-code
QualifyingResultExample = {
    "timestamp": 1669984487.606552,
    "results": [
        {
            "timestamp": None,
            "number": 1,
            "position": 1,
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
            "Q1": "1:24.754",
            "Q2": "1:24.622",
            "Q3": "1:23.824"
        },
        {
            "timestamp": None,
            "number": 11,
            "position": 2,
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
            "Q1": "1:24.820",
            "Q2": "1:24.419",
            "Q3": "1:24.052"
        },
        {
            "timestamp": None,
            "number": 16,
            "position": 3,
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
            "Q1": "1:25.211",
            "Q2": "1:24.517",
            "Q3": "1:24.092"
        },
        {
            "timestamp": None,
            "number": 55,
            "position": 4,
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
            "Q1": "1:25.090",
            "Q2": "1:24.521",
            "Q3": "1:24.242"
        },
        {
            "timestamp": None,
            "number": 44,
            "position": 5,
            "Driver": {
                "timestamp": None,
                "driverId": "hamilton",
                "url": "https://en.wikipedia.org/wiki/Lewis_Hamilton",
                "givenName": "Lewis",
                "familyName": "Hamilton",
                "dateOfBirth": "1985-01-07",
                "nationality": "British",
                "permanentNumber": 44,
                "code": "HAM"
            },
            "Constructor": {
                "timestamp": None,
                "constructorId": "mercedes",
                "url": "https://en.wikipedia.org/wiki/Mercedes-Benz_in_Formula_One",
                "name": "Mercedes",
                "nationality": "German"
            },
            "Q1": "1:25.594",
            "Q2": "1:24.774",
            "Q3": "1:24.508"
        }
    ]
}
