import os

from fastapi import APIRouter

from app.internal.logic.cache_init import get_cache, invalidate_cache
from app.internal.logic.errors import service_unavailable, data_not_found
from app.internal.models.f1.constructor import Constructor, Constructors, ConstructorExample, ConstructorsExample
from app.internal.models.general.message import Message, create_message

router = APIRouter(
    tags=["Constructors"],
)


# CONSTRUCTORS
# https://ergast.com/mrd/methods/constructors/

@router.get("/constructors",
            response_model=Constructors,
            responses={
                404: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Constructors not found")
                    }
                }},
                503: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Service unavailable")
                    }
                }},
                200: {"model": Constructors, "content": {
                    "application/json": {
                        "example": ConstructorsExample
                    }
                }}
            })
async def get_constructors():
    data, timestamp = get_cache(f"{os.getenv('ERGAST_API')}/api/f1/constructors.json?limit=300",
                                "get_constructors")

    try:
        if len(data["MRData"]["ConstructorTable"]["Constructors"]) <= 0:
            raise IndexError

        constructors = {"constructors": data["MRData"]["ConstructorTable"]["Constructors"], "timestamp": timestamp}
    except IndexError:
        invalidate_cache("get_constructors")
        return data_not_found("Constructors")
    except KeyError:
        invalidate_cache("get_constructors")
        return service_unavailable()

    return constructors


@router.get("/constructors/{season}",
            tags=["Season"],
            response_model=Constructors,
            responses={
                404: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Constructors not found")
                    }
                }},
                503: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Service unavailable")
                    }
                }},
                200: {"model": Constructors, "content": {
                    "application/json": {
                        "example": ConstructorsExample
                    }
                }}
            })
async def get_constructors_by_season(season: str):
    data, timestamp = get_cache(f"{os.getenv('ERGAST_API')}/api/f1/{season}/constructors.json?limit=300",
                                f"get_constructors_by_season.{season}")

    try:
        if len(data["MRData"]["ConstructorTable"]["Constructors"]) <= 0:
            raise IndexError

        constructors = {"constructors": data["MRData"]["ConstructorTable"]["Constructors"], "timestamp": timestamp}
    except IndexError:
        invalidate_cache(f"get_constructors_by_season.{season}")
        return data_not_found("Constructors")
    except KeyError:
        invalidate_cache(f"get_constructors_by_season.{season}")
        return service_unavailable()

    return constructors


@router.get("/constructor/{constructor_id}",
            response_model=Constructor,
            responses={
                404: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Constructor not found")
                    }
                }},
                503: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Service unavailable")
                    }
                }},
                200: {"model": Constructor, "content": {
                    "application/json": {
                        "example": ConstructorExample
                    }
                }}
            })
async def get_constructor_by_id(constructor_id: str):
    data, timestamp = get_cache(f"{os.getenv('ERGAST_API')}/api/f1/constructors/{constructor_id}.json",
                                f"get_constructor_by_id.{constructor_id}")

    try:
        constructor = data["MRData"]["ConstructorTable"]["Constructors"][0]
        constructor["timestamp"] = timestamp
    except IndexError:
        invalidate_cache(f"get_constructor_by_id.{constructor_id}")
        return data_not_found("Constructor")
    except KeyError:
        invalidate_cache(f"get_constructor_by_id.{constructor_id}")
        return service_unavailable()

    return constructor
