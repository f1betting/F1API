from pydantic import BaseModel

from app.internal.models.general.request import BaseRequest


class Location(BaseModel):
    lat: float
    long: float
    locality: str
    country: str


class Circuit(BaseRequest):
    circuitId: str
    url: str
    circuitName: str
    Location: Location


class Circuits(BaseRequest):
    circuits: list[Circuit]


# pylint: disable=duplicate-code
CircuitExample = {
    "timestamp": 1669978998.3723269,
    "circuitId": "zandvoort",
    "url": "https://en.wikipedia.org/wiki/Circuit_Zandvoort",
    "circuitName": "Circuit Park Zandvoort",
    "Location": {
        "lat": 52.3888,
        "long": 4.54092,
        "locality": "Zandvoort",
        "country": "Netherlands"
    }
}

CircuitsExample = {
    "timestamp": 1669984523.7729688,
    "circuits": [
        {
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
        {
            "timestamp": None,
            "circuitId": "americas",
            "url": "https://en.wikipedia.org/wiki/Circuit_of_the_Americas",
            "circuitName": "Circuit of the Americas",
            "Location": {
                "lat": 30.1328,
                "long": -97.6411,
                "locality": "Austin",
                "country": "USA"
            }
        },
        {
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
        {
            "timestamp": None,
            "circuitId": "baku",
            "url": "https://en.wikipedia.org/wiki/Baku_City_Circuit",
            "circuitName": "Baku City Circuit",
            "Location": {
                "lat": 40.3725,
                "long": 49.8533,
                "locality": "Baku",
                "country": "Azerbaijan"
            }
        },
        {
            "timestamp": None,
            "circuitId": "catalunya",
            "url": "https://en.wikipedia.org/wiki/Circuit_de_Barcelona-Catalunya",
            "circuitName": "Circuit de Barcelona-Catalunya",
            "Location": {
                "lat": 41.57,
                "long": 2.26111,
                "locality": "Montmeló",
                "country": "Spain"
            }
        }
    ]
}
