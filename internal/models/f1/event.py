from pydantic import BaseModel

from internal.models.f1.circuit import Circuit
from internal.models.f1.internal.session import Session


class Event(BaseModel):
    season: int
    round: int
    url: str
    raceName: str
    Circuit: Circuit
    date: str
    time: str | None
    FirstPractice: Session | None
    SecondPractice: Session | None
    ThirdPractice: Session | None
    Qualifying: Session | None


class Calendar(BaseModel):
    events: list[Event]


class NextEvent(BaseModel):
    season: int
    round: int


EventExample = {
    "season": 2022,
    "round": 1,
    "url": "http://en.wikipedia.org/wiki/2022_Bahrain_Grand_Prix",
    "raceName": "Bahrain Grand Prix",
    "Circuit": {
        "circuitId": "bahrain",
        "url": "http://en.wikipedia.org/wiki/Bahrain_International_Circuit",
        "circuitName": "Bahrain International Circuit",
        "Location": {
            "lat": 26.0325,
            "long": 50.5106,
            "locality": "Sakhir",
            "country": "Bahrain"
        }
    },
    "date": "2022-03-20",
    "time": "15:00:00Z",
    "FirstPractice": {
        "date": "2022-03-18",
        "time": "12:00:00Z"
    },
    "SecondPractice": {
        "date": "2022-03-18",
        "time": "15:00:00Z"
    },
    "ThirdPractice": {
        "date": "2022-03-19",
        "time": "12:00:00Z"
    },
    "Qualifying": {
        "date": "2022-03-19",
        "time": "15:00:00Z"
    }
}

NextEventExample = {
    "season": 2022,
    "round": 17,
}
