from pydantic import BaseModel


class Constructor(BaseModel):
    constructorId: str
    url: str
    name: str
    nationality: str


ConstructorExample = {
    "constructorId": "red_bull",
    "url": "http://en.wikipedia.org/wiki/Red_Bull_Racing",
    "name": "Red Bull",
    "nationality": "Austrian"
}
