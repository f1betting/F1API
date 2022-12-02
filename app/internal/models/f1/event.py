from app.internal.models.f1.circuit import Circuit
from app.internal.models.f1.internal.session import Session
from app.internal.models.general.request import BaseRequest


class Event(BaseRequest):
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


class Calendar(BaseRequest):
    events: list[Event]


class NextEvent(BaseRequest):
    season: int
    round: int


# pylint: disable=duplicate-code
EventExample = {
    "timestamp": 1669979237.0388148,
    "season": 2022,
    "round": 22,
    "url": "https://en.wikipedia.org/wiki/2022_Abu_Dhabi_Grand_Prix",
    "raceName": "Abu Dhabi Grand Prix",
    "Circuit": {
        "timestamp": None,
        "circuitId": "yas_marina",
        "url": "https://en.wikipedia.org/wiki/Yas_Marina_Circuit",
        "circuitName": "Yas Marina Circuit",
        "Location": {
            "lat": 24.4672,
            "long": 54.6031,
            "locality": "Abu Dhabi",
            "country": "UAE"
        }
    },
    "date": "2022-11-20",
    "time": "13:00:00Z",
    "FirstPractice": {
        "date": "2022-11-18",
        "time": "10:00:00Z"
    },
    "SecondPractice": {
        "date": "2022-11-18",
        "time": "13:00:00Z"
    },
    "ThirdPractice": {
        "date": "2022-11-19",
        "time": "11:00:00Z"
    },
    "Qualifying": {
        "date": "2022-11-19",
        "time": "14:00:00Z"
    }
}

# pylint: disable=duplicate-code
CalendarExample = {
    "timestamp": 1669979281.7311087,
    "events": [
        {
            "timestamp": None,
            "season": 2022,
            "round": 1,
            "url": "https://en.wikipedia.org/wiki/2022_Bahrain_Grand_Prix",
            "raceName": "Bahrain Grand Prix",
            "Circuit": {
                "timestamp": None,
                "circuitId": "bahrain",
                "url": "https://en.wikipedia.org/wiki/Bahrain_International_Circuit",
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
        },
    ]
}

# pylint: disable=duplicate-code
NextEventExample = {
    "timestamp": 1669979205.6921754,
    "season": 2023,
    "round": 1
}
