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
    "timestamp": 1669984214.2694075,
    "constructors": [
        {
            "timestamp": None,
            "constructorId": "alfa",
            "url": "https://en.wikipedia.org/wiki/Alfa_Romeo_in_Formula_One",
            "name": "Alfa Romeo",
            "nationality": "Swiss"
        },
        {
            "timestamp": None,
            "constructorId": "alphatauri",
            "url": "https://en.wikipedia.org/wiki/Scuderia_AlphaTauri",
            "name": "AlphaTauri",
            "nationality": "Italian"
        },
        {
            "timestamp": None,
            "constructorId": "alpine",
            "url": "https://en.wikipedia.org/wiki/Alpine_F1_Team",
            "name": "Alpine F1 Team",
            "nationality": "French"
        },
        {
            "timestamp": None,
            "constructorId": "aston_martin",
            "url": "https://en.wikipedia.org/wiki/Aston_Martin_in_Formula_One",
            "name": "Aston Martin",
            "nationality": "British"
        },
        {
            "timestamp": None,
            "constructorId": "ferrari",
            "url": "https://en.wikipedia.org/wiki/Scuderia_Ferrari",
            "name": "Ferrari",
            "nationality": "Italian"
        }
    ]
}
