from pydantic import BaseModel


class Location(BaseModel):
    lat: float
    long: float
    locality: str
    country: str


class Circuit(BaseModel):
    circuitId: str
    url: str
    circuitName: str
    Location: Location


CircuitExample = {
    "circuitId": "zandvoort",
    "url": "http://en.wikipedia.org/wiki/Circuit_Zandvoort",
    "circuitName": "Circuit Park Zandvoort",
    "Location": {
        "lat": 52.3888,
        "long": 4.54092,
        "locality": "Zandvoort",
        "country": "Netherlands"
    }
}
