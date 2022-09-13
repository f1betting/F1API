import requests
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from classes.f1.driver import Driver, Drivers, DriverExample
from classes.general.message import Message

router = APIRouter(
    tags=["Drivers"],
)


# DRIVERS
# https://ergast.com/mrd/methods/drivers/

@router.get("/drivers",
            response_model=Drivers,
            responses={
                404: {"model": Message, "description": "Drivers not found"},
                200: {"model": Driver, "content": {
                    "application/json": {
                        "example": [
                            DriverExample
                        ]
                    }
                }}
            })
async def get_drivers():
    url = f"https://ergast.com/api/f1/drivers.json?limit=1000"
    res = requests.get(url)
    data = res.json()
    drivers = data["MRData"]["DriverTable"]["Drivers"]

    if not drivers:
        return JSONResponse(status_code=404, content={"message": "Drivers not found"})

    return drivers


@router.get("/drivers/{season}",
            tags=["Season"],
            response_model=Drivers,
            responses={
                404: {"model": Message, "description": "Drivers not found"},
                200: {"model": Driver, "content": {
                    "application/json": {
                        "example": [
                            DriverExample
                        ]
                    }
                }}
            })
async def get_drivers_by_season(season: str):
    url = f"https://ergast.com/api/f1/{season}/drivers.json?limit=1000"
    res = requests.get(url)
    data = res.json()
    drivers = data["MRData"]["DriverTable"]["Drivers"]

    if not drivers:
        return JSONResponse(status_code=404, content={"message": "Drivers not found"})

    return drivers


@router.get("/driver/{driver_id}",
            response_model=Driver,
            responses={
                404: {"model": Message, "description": "Driver not found"},
                200: {"model": Driver, "content": {
                    "application/json": {
                        "example": DriverExample
                    }
                }}
            })
async def get_driver_by_id(driver_id: str):
    url = f"https://ergast.com/api/f1/drivers/{driver_id}.json"
    res = requests.get(url)
    data = res.json()
    driver = data["MRData"]["DriverTable"]["Drivers"]

    if not driver:
        return JSONResponse(status_code=404, content={"message": "Driver not found"})

    return driver[0]
