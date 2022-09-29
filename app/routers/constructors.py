import requests
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.internal.models.f1.constructor import Constructor, Constructors, ConstructorExample
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
    url = f"https://ergast.com/api/f1/constructors.json?limit=300"
    res = requests.get(url)
    data = res.json()
    constructors = data["MRData"]["ConstructorTable"]["Constructors"]

    if not constructors:
        return JSONResponse(status_code=404, content=create_message("Constructors not found"))

    return {"constructors": constructors}


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
    url = f"https://ergast.com/api/f1/{season}/constructors.json?limit=300"
    res = requests.get(url)
    data = res.json()
    constructors = data["MRData"]["ConstructorTable"]["Constructors"]

    if not constructors:
        return JSONResponse(status_code=404, content=create_message("Constructors not found"))

    return {"constructors": constructors}


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
    url = f"https://ergast.com/api/f1/constructors/{constructor_id}.json"
    res = requests.get(url)
    data = res.json()
    constructor = data["MRData"]["ConstructorTable"]["Constructors"]

    if not constructor:
        return JSONResponse(status_code=404, content=create_message("Constructor not found"))

    return constructor[0]
