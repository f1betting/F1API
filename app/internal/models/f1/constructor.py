from app.internal.models.general.request import BaseRequest


class Constructor(BaseRequest):
    constructorId: str
    url: str
    name: str
    nationality: str


class Constructors(BaseRequest):
    constructors: list[Constructor]


# pylint: disable=duplicate-code
ConstructorExample = {
    "timestamp": 1669978904.85484,
    "constructorId": "red_bull",
    "url": "https://en.wikipedia.org/wiki/Red_Bull_Racing",
    "name": "Red Bull",
    "nationality": "Austrian"
}

ConstructorsExample = {
    "timestamp": 1669978869.9509943,
    "constructors": [
        {
            "timestamp": None,
            "constructorId": "red_bull",
            "url": "https://en.wikipedia.org/wiki/Red_Bull_Racing",
            "name": "Red Bull",
            "nationality": "Austrian"
        }
    ]
}
