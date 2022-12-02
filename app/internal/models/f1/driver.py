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
    "timestamp": 1669984067.7710564,
    "drivers": [
        {
            "timestamp": None,
            "driverId": "albon",
            "url": "https://en.wikipedia.org/wiki/Alexander_Albon",
            "givenName": "Alexander",
            "familyName": "Albon",
            "dateOfBirth": "1996-03-23",
            "nationality": "Thai",
            "permanentNumber": 23,
            "code": "ALB"
        },
        {
            "timestamp": None,
            "driverId": "alonso",
            "url": "https://en.wikipedia.org/wiki/Fernando_Alonso",
            "givenName": "Fernando",
            "familyName": "Alonso",
            "dateOfBirth": "1981-07-29",
            "nationality": "Spanish",
            "permanentNumber": 14,
            "code": "ALO"
        },
        {
            "timestamp": None,
            "driverId": "bottas",
            "url": "https://en.wikipedia.org/wiki/Valtteri_Bottas",
            "givenName": "Valtteri",
            "familyName": "Bottas",
            "dateOfBirth": "1989-08-28",
            "nationality": "Finnish",
            "permanentNumber": 77,
            "code": "BOT"
        },
        {
            "timestamp": None,
            "driverId": "de_vries",
            "url": "https://en.wikipedia.org/wiki/Nyck_de_Vries",
            "givenName": "Nyck",
            "familyName": "de Vries",
            "dateOfBirth": "1995-02-06",
            "nationality": "Dutch",
            "permanentNumber": 45,
            "code": "DEV"
        },
        {
            "timestamp": None,
            "driverId": "gasly",
            "url": "https://en.wikipedia.org/wiki/Pierre_Gasly",
            "givenName": "Pierre",
            "familyName": "Gasly",
            "dateOfBirth": "1996-02-07",
            "nationality": "French",
            "permanentNumber": 10,
            "code": "GAS"
        }
    ]
}
