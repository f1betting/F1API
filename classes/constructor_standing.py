from pydantic import BaseModel
from classes.constructor import Constructor
from classes.driver import Driver


class ConstructorStanding(BaseModel):
    position: int
    positionText: str
    points: int
    wins: int
    Constructor: Constructor


ConstructorStandingsExample = {
    "position": "1",
    "positionText": "1",
    "points": "545",
    "wins": "12",
    "Constructor": {
        "constructorId": "red_bull",
        "url": "http://en.wikipedia.org/wiki/Red_Bull_Racing",
        "name": "Red Bull",
        "nationality": "Austrian"
    }
}
