from app.internal.models.general.request import BaseRequest


class Driver(BaseRequest):
    driverId: str
    url: str
    givenName: str
    familyName: str
    dateOfBirth: str
    nationality: str
    permanentNumber: int | None
    code: str | None


class Drivers(BaseRequest):
    drivers: list[Driver]


# pylint: disable=duplicate-code
DriverExample = {
    "timestamp": 1669978482.9627361,
    "driverId": "max_verstappen",
    "url": "https://en.wikipedia.org/wiki/Max_Verstappen",
    "givenName": "Max",
    "familyName": "Verstappen",
    "dateOfBirth": "1997-09-30",
    "nationality": "Dutch",
    "permanentNumber": 33,
    "code": "VER"
}

DriversExample = {
    "timestamp": 1669978500.8190658,
    "drivers": [
        {
            "timestamp": None,
            "driverId": "max_verstappen",
            "url": "https://en.wikipedia.org/wiki/Max_Verstappen",
            "givenName": "Max",
            "familyName": "Verstappen",
            "dateOfBirth": "1997-09-30",
            "nationality": "Dutch",
            "permanentNumber": 33,
            "code": "VER"
        }
    ]
}
