import os

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.internal.logic.cache_init import get_cache, invalidate_cache
from app.internal.logic.errors import service_unavailable, data_not_found
from app.internal.models.f1.driver import Driver, Drivers, DriverExample
from app.internal.models.general.message import Message, create_message

router = APIRouter(
    tags=["Drivers"],
)


# DRIVERS
# https://ergast.com/mrd/methods/drivers/

@router.get("/drivers",
            response_model=Drivers,
            responses={
                404: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Drivers not found")
                    }
                }},
                503: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Service unavailable")
                    }
                }},
                200: {"model": Drivers, "content": {
                    "application/json": {
                        "example": {
                            "drivers": [
                                DriverExample
                            ]
                        }
                    }
                }}
            })
async def get_drivers():
    data, timestamp = get_cache(f"{os.getenv('ERGAST_API')}/api/f1/drivers.json?limit=1000",
                                f"get_drivers")

    try:
        if len(data["MRData"]["DriverTable"]["Drivers"]) <= 0:
            raise IndexError

        drivers = {"drivers": data["MRData"]["DriverTable"]["Drivers"], "timestamp": timestamp}
    except IndexError:
        invalidate_cache("get_drivers")
        return data_not_found("Drivers")
    except KeyError:
        invalidate_cache("get_drivers")
        return service_unavailable()

    return drivers


@router.get("/drivers/{season}",
            tags=["Season"],
            response_model=Drivers,
            responses={
                404: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Drivers not found")
                    }
                }},
                503: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Service unavailable")
                    }
                }},
                200: {"model": Drivers, "content": {
                    "application/json": {
                        "example": {
                            "drivers": [
                                DriverExample
                            ]
                        }
                    }
                }}
            })
async def get_drivers_by_season(season: int):
    data, timestamp = get_cache(f"{os.getenv('ERGAST_API')}/api/f1/{season}/drivers.json?limit=1000",
                                f"get_drivers_by_season.{season}")

    try:
        if len(data["MRData"]["DriverTable"]["Drivers"]) <= 0:
            raise IndexError

        drivers = {"drivers": data["MRData"]["DriverTable"]["Drivers"], "timestamp": timestamp}
    except IndexError:
        invalidate_cache(f"get_drivers_by_season.{season}")
        return data_not_found("Drivers")
    except KeyError:
        invalidate_cache(f"get_drivers_by_season.{season}")
        return service_unavailable()

    return drivers


@router.get("/driver/{driver_id}",
            response_model=Driver,
            responses={
                404: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Driver not found")
                    }
                }},
                503: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Service unavailable")
                    }
                }},
                200: {"model": Driver, "content": {
                    "application/json": {
                        "example": DriverExample
                    }
                }}
            })
async def get_driver_by_id(driver_id: str):
    data, timestamp = get_cache(f"{os.getenv('ERGAST_API')}/api/f1/drivers/{driver_id}.json",
                                f"get_driver_by_id.{driver_id}")

    try:
        driver = data["MRData"]["DriverTable"]["Drivers"][0]
        driver["timestamp"] = timestamp
    except IndexError:
        invalidate_cache(f"get_driver_by_id.{driver_id}")
        return data_not_found("Driver")
    except KeyError:
        invalidate_cache(f"get_driver_by_id.{driver_id}")
        return service_unavailable()

    return driver
