from pydantic import BaseModel


class Driver(BaseModel):
    driverId: str
    url: str
    givenName: str
    familyName: str
    dateOfBirth: str
    nationality: str
    permanentNumber: int | None
    code: str | None


class Drivers(BaseModel):
    drivers: list[Driver]


DriverExample = {
    "driverId": "max_verstappen",
    "url": "http://en.wikipedia.org/wiki/Max_Verstappen",
    "givenName": "Max",
    "familyName": "Verstappen",
    "dateOfBirth": "1997-09-30",
    "nationality": "Dutch",
    "permanentNumber": 33,
    "code": "VER"
}
