from app.internal.models.f1.constructor import Constructor
from app.internal.models.general.request import BaseRequest


class ConstructorStanding(BaseRequest):
    position: int
    positionText: str
    points: int
    wins: int
    Constructor: Constructor


class ConstructorStandings(BaseRequest):
    standings: list[ConstructorStanding]


ConstructorStandingsExample = {
    "position": 1,
    "positionText": "1",
    "points": 545,
    "wins": 12,
    "Constructor": {
        "constructorId": "red_bull",
        "url": "http://en.wikipedia.org/wiki/Red_Bull_Racing",
        "name": "Red Bull",
        "nationality": "Austrian"
    }
}
