from pydantic import BaseModel
from classes.constructor import Constructor
from classes.driver import Driver


class QualifyingResult(BaseModel):
    number: int
    position: int
    Driver: Driver
    Constructor: Constructor
    Q1: str | None
    Q2: str | None
    Q3: str | None


class QualifyingResults(list[QualifyingResult]):
    pass


QualifyingResultExample = {
    "number": 1,
    "position": 1,
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
    "Q1": "1:19.295",
    "Q2": "1:18.793",
    "Q3": "1:27.999"
}
