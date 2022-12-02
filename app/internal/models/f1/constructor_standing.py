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


# pylint: disable=duplicate-code
ConstructorStandingsExample = {
    "timestamp": 1669977723.5049899,
    "standings": [
        {
            "timestamp": None,
            "position": 1,
            "positionText": "1",
            "points": 759,
            "wins": 17,
            "Constructor": {
                "timestamp": None,
                "constructorId": "red_bull",
                "url": "https://en.wikipedia.org/wiki/Red_Bull_Racing",
                "name": "Red Bull",
                "nationality": "Austrian"
            }
        },
    ]
}
