import requests
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from classes.constructor import Constructor, ConstructorExample
from classes.message import Message

router = APIRouter(
    tags=["Constructors"],
)


# CONSTRUCTORS
# https://ergast.com/mrd/methods/constructors/

@router.get("/constructors",
            response_model=list[Constructor],
            responses={
                404: {"model": Message, "description": "Constructors not found"},
                200: {"model": Constructor, "content": {
                    "application/json": {
                        "example": [
                            ConstructorExample
                        ]
                    }
                }}
            })
async def get_constructors():
    url = f"https://ergast.com/api/f1/constructors.json?limit=300"
    res = requests.get(url)
    data = res.json()
    constructors = data["MRData"]["ConstructorTable"]["Constructors"]

    if not constructors:
        return JSONResponse(status_code=404, content={"message": "Constructors not found"})

    return constructors


@router.get("/constructors/{season}",
            tags=["Season"],
            response_model=list[Constructor],
            responses={
                404: {"model": Message, "description": "Constructors not found"},
                200: {"model": Constructor, "content": {
                    "application/json": {
                        "example": [
                            ConstructorExample
                        ]
                    }
                }}
            })
async def get_constructors_by_season(season: str):
    url = f"https://ergast.com/api/f1/{season}/constructors.json?limit=300"
    res = requests.get(url)
    data = res.json()
    constructors = data["MRData"]["ConstructorTable"]["Constructors"]

    if not constructors:
        return JSONResponse(status_code=404, content={"message": "Constructors not found"})

    return constructors


@router.get("/constructor/{constructor_id}",
            response_model=Constructor,
            responses={
                404: {"model": Message, "description": "Constructor not found"},
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
        return JSONResponse(status_code=404, content={"message": "Constructor not found"})

    return constructor[0]
