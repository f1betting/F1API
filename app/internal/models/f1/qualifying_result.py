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
    "timestamp": 1669978379.0060742,
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
        }
    ]
}
