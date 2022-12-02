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
    "timestamp": 1669984250.8745742,
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
        {
            "timestamp": None,
            "position": 2,
            "positionText": "2",
            "points": 554,
            "wins": 4,
            "Constructor": {
                "timestamp": None,
                "constructorId": "ferrari",
                "url": "https://en.wikipedia.org/wiki/Scuderia_Ferrari",
                "name": "Ferrari",
                "nationality": "Italian"
            }
        },
        {
            "timestamp": None,
            "position": 3,
            "positionText": "3",
            "points": 515,
            "wins": 1,
            "Constructor": {
                "timestamp": None,
                "constructorId": "mercedes",
                "url": "https://en.wikipedia.org/wiki/Mercedes-Benz_in_Formula_One",
                "name": "Mercedes",
                "nationality": "German"
            }
        },
        {
            "timestamp": None,
            "position": 4,
            "positionText": "4",
            "points": 173,
            "wins": 0,
            "Constructor": {
                "timestamp": None,
                "constructorId": "alpine",
                "url": "https://en.wikipedia.org/wiki/Alpine_F1_Team",
                "name": "Alpine F1 Team",
                "nationality": "French"
            }
        },
        {
            "timestamp": None,
            "position": 5,
            "positionText": "5",
            "points": 159,
            "wins": 0,
            "Constructor": {
                "timestamp": None,
                "constructorId": "mclaren",
                "url": "https://en.wikipedia.org/wiki/McLaren",
                "name": "McLaren",
                "nationality": "British"
            }
        }
    ]
}
