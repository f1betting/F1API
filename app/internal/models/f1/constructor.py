from app.internal.models.general.request import BaseRequest


class Constructor(BaseRequest):
    constructorId: str
    url: str
    name: str
    nationality: str


class Constructors(BaseRequest):
    constructors: list[Constructor]


ConstructorExample = {
    "constructorId": "red_bull",
    "url": "https://://en.wikipedia.org/wiki/Red_Bull_Racing",
    "name": "Red Bull",
    "nationality": "Austrian"
}
