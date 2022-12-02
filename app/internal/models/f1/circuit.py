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
    "timestamp": 1669978972.4221265,
    "circuits": [
        {
            "timestamp": None,
            "circuitId": "zandvoort",
            "url": "https://en.wikipedia.org/wiki/Circuit_Zandvoort",
            "circuitName": "Circuit Park Zandvoort",
            "Location": {
                "lat": 52.3888,
                "long": 4.54092,
                "locality": "Zandvoort",
                "country": "Netherlands"
            }
        },
    ]
}
