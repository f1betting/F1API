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
    "timestamp": 1669984351.4048898,
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
        {
            "timestamp": None,
            "season": 2022,
            "round": 2,
            "url": "https://en.wikipedia.org/wiki/2022_Saudi_Arabian_Grand_Prix",
            "raceName": "Saudi Arabian Grand Prix",
            "Circuit": {
                "timestamp": None,
                "circuitId": "jeddah",
                "url": "https://en.wikipedia.org/wiki/Jeddah_Street_Circuit",
                "circuitName": "Jeddah Corniche Circuit",
                "Location": {
                    "lat": 21.6319,
                    "long": 39.1044,
                    "locality": "Jeddah",
                    "country": "Saudi Arabia"
                }
            },
            "date": "2022-03-27",
            "time": "17:00:00Z",
            "FirstPractice": {
                "date": "2022-03-25",
                "time": "14:00:00Z"
            },
            "SecondPractice": {
                "date": "2022-03-25",
                "time": "17:00:00Z"
            },
            "ThirdPractice": {
                "date": "2022-03-26",
                "time": "14:00:00Z"
            },
            "Qualifying": {
                "date": "2022-03-26",
                "time": "17:00:00Z"
            }
        },
        {
            "timestamp": None,
            "season": 2022,
            "round": 3,
            "url": "https://en.wikipedia.org/wiki/2022_Australian_Grand_Prix",
            "raceName": "Australian Grand Prix",
            "Circuit": {
                "timestamp": None,
                "circuitId": "albert_park",
                "url": "https://en.wikipedia.org/wiki/Melbourne_Grand_Prix_Circuit",
                "circuitName": "Albert Park Grand Prix Circuit",
                "Location": {
                    "lat": -37.8497,
                    "long": 144.968,
                    "locality": "Melbourne",
                    "country": "Australia"
                }
            },
            "date": "2022-04-10",
            "time": "05:00:00Z",
            "FirstPractice": {
                "date": "2022-04-08",
                "time": "03:00:00Z"
            },
            "SecondPractice": {
                "date": "2022-04-08",
                "time": "06:00:00Z"
            },
            "ThirdPractice": {
                "date": "2022-04-09",
                "time": "03:00:00Z"
            },
            "Qualifying": {
                "date": "2022-04-09",
                "time": "06:00:00Z"
            }
        },
        {
            "timestamp": None,
            "season": 2022,
            "round": 4,
            "url": "https://en.wikipedia.org/wiki/2022_Emilia_Romagna_Grand_Prix",
            "raceName": "Emilia Romagna Grand Prix",
            "Circuit": {
                "timestamp": None,
                "circuitId": "imola",
                "url": "https://en.wikipedia.org/wiki/Autodromo_Enzo_e_Dino_Ferrari",
                "circuitName": "Autodromo Enzo e Dino Ferrari",
                "Location": {
                    "lat": 44.3439,
                    "long": 11.7167,
                    "locality": "Imola",
                    "country": "Italy"
                }
            },
            "date": "2022-04-24",
            "time": "13:00:00Z",
            "FirstPractice": {
                "date": "2022-04-22",
                "time": "11:30:00Z"
            },
            "SecondPractice": {
                "date": "2022-04-23",
                "time": "10:30:00Z"
            },
            "ThirdPractice": None,
            "Qualifying": {
                "date": "2022-04-22",
                "time": "15:00:00Z"
            }
        },
        {
            "timestamp": None,
            "season": 2022,
            "round": 5,
            "url": "https://en.wikipedia.org/wiki/2022_Miami_Grand_Prix",
            "raceName": "Miami Grand Prix",
            "Circuit": {
                "timestamp": None,
                "circuitId": "miami",
                "url": "https://en.wikipedia.org/wiki/Miami_International_Autodrome",
                "circuitName": "Miami International Autodrome",
                "Location": {
                    "lat": 25.9581,
                    "long": -80.2389,
                    "locality": "Miami",
                    "country": "USA"
                }
            },
            "date": "2022-05-08",
            "time": "19:30:00Z",
            "FirstPractice": {
                "date": "2022-05-06",
                "time": "18:30:00Z"
            },
            "SecondPractice": {
                "date": "2022-05-06",
                "time": "21:30:00Z"
            },
            "ThirdPractice": {
                "date": "2022-05-07",
                "time": "17:00:00Z"
            },
            "Qualifying": {
                "date": "2022-05-07",
                "time": "20:00:00Z"
            }
        }
    ]
}

# pylint: disable=duplicate-code
NextEventExample = {
    "timestamp": 1669979205.6921754,
    "season": 2023,
    "round": 1
}
