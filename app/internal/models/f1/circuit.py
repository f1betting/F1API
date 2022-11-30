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
    "circuitId": "zandvoort",
    "url": "https://://en.wikipedia.org/wiki/Circuit_Zandvoort",
    "circuitName": "Circuit Park Zandvoort",
    "Location": {
        "lat": 52.3888,
        "long": 4.54092,
        "locality": "Zandvoort",
        "country": "Netherlands"
    }
}
