from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.internal.logic.cache_init import get_cache
from app.internal.models.f1.constructor import Constructor, Constructors, ConstructorExample
from app.internal.models.general.message import Message, create_message

router = APIRouter(
    tags=["Constructors"],
)


# CONSTRUCTORS
# http://185.229.22.110/mrd/methods/constructors/

@router.get("/constructors",
            response_model=Constructors,
            responses={
                404: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Constructors not found")
                    }
                }},
                200: {"model": Constructors, "content": {
                    "application/json": {
                        "example": {
                            "constructors": [
                                ConstructorExample
                            ]
                        }
                    }
                }}
            })
async def get_constructors():
    data, timestamp = get_cache("http://185.229.22.110/api/f1/constructors.json?limit=300",
                                "get_constructors")

    constructors = {"constructors": data["MRData"]["ConstructorTable"]["Constructors"], "timestamp": timestamp}

    if not constructors["constructors"]:
        return JSONResponse(status_code=404, content=create_message("Constructors not found"))

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
                200: {"model": Constructors, "content": {
                    "application/json": {
                        "example": {
                            "constructors": [
                                ConstructorExample
                            ]
                        }
                    }
                }}
            })
async def get_constructors_by_season(season: str):
    data, timestamp = get_cache(f"http://185.229.22.110/api/f1/{season}/constructors.json?limit=300",
                                f"get_constructors_by_season.{season}")

    constructors = {"constructors": data["MRData"]["ConstructorTable"]["Constructors"], "timestamp": timestamp}

    if not constructors["constructors"]:
        return JSONResponse(status_code=404, content=create_message("Constructors not found"))

    return constructors


@router.get("/constructor/{constructor_id}",
            response_model=Constructor,
            responses={
                404: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Constructor not found")
                    }
                }},
                200: {"model": Constructor, "content": {
                    "application/json": {
                        "example": ConstructorExample
                    }
                }}
            })
async def get_constructor_by_id(constructor_id: str):
    data, timestamp = get_cache(f"http://185.229.22.110/api/f1/constructors/{constructor_id}.json",
                                f"get_constructor_by_id.{constructor_id}")

    try:
        constructor = data["MRData"]["ConstructorTable"]["Constructors"][0]
        constructor["timestamp"] = timestamp
    except IndexError:
        return JSONResponse(status_code=404, content=create_message("Constructor not found"))

    return constructor
