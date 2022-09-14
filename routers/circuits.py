import requests
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from classes.f1.circuit import Circuit, Circuits, CircuitExample
from classes.general.message import Message, create_message

router = APIRouter(
    tags=["Circuits"]
)


# CIRCUITS
# https://ergast.com/mrd/methods/circuits/

@router.get("/circuits",
            response_model=Circuits,
            responses={
                404: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Circuits not found")
                    }
                }},
                200: {"model": Circuit, "content": {
                    "application/json": {
                        "example": {
                            "circuits": [
                                CircuitExample
                            ]
                        }
                    }
                }}
            })
async def get_circuits():
    url = f"https://ergast.com/api/f1/circuits.json?limit=100"
    res = requests.get(url)
    data = res.json()
    circuits = data["MRData"]["CircuitTable"]["Circuits"]

    if not circuits:
        return JSONResponse(status_code=404, content=create_message("Circuits not found"))

    return {"circuits": circuits}


@router.get("/circuits/{season}",
            tags=["Season"],
            response_model=Circuits,
            responses={
                404: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Circuits not found")
                    }
                }},
                200: {"model": Circuit, "content": {
                    "application/json": {
                        "example": {
                            "circuits": [
                                CircuitExample
                            ]
                        }
                    }
                }}
            })
async def get_circuits_by_season(season: str):
    url = f"https://ergast.com/api/f1/{season}/circuits.json?limit=100"
    res = requests.get(url)
    data = res.json()
    circuits = data["MRData"]["CircuitTable"]["Circuits"]

    if not circuits:
        return JSONResponse(status_code=404, content=create_message("Circuits not found"))

    return {"circuits": circuits}


@router.get("/circuit/{circuit_id}",
            response_model=Circuit,
            responses={
                404: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Circuit not found")
                    }
                }},
                200: {"model": Circuit, "content": {
                    "application/json": {
                        "example": CircuitExample
                    }
                }}
            })
async def get_circuit_by_id(circuit_id: str):
    url = f"https://ergast.com/api/f1/circuits/{circuit_id}.json"
    res = requests.get(url)
    data = res.json()
    circuit = data["MRData"]["CircuitTable"]["Circuits"]

    if not circuit:
        return JSONResponse(status_code=404, content=create_message("Circuit not found"))

    return circuit[0]
