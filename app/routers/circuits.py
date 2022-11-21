import requests
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.internal.logic.cache_init import get_cache
from app.internal.models.f1.circuit import Circuit, Circuits, CircuitExample
from app.internal.models.general.message import Message, create_message

router = APIRouter(
    tags=["Circuits"]
)


# CIRCUITS
# http://185.229.22.110/mrd/methods/circuits/

@router.get("/circuits",
            response_model=Circuits,
            responses={
                404: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Circuits not found")
                    }
                }},
                200: {"model": Circuits, "content": {
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
    data, timestamp = get_cache("http://185.229.22.110/api/f1/circuits.json?limit=100", "get_circuits")

    try:
        circuits = {"circuits": data["MRData"]["CircuitTable"]["Circuits"], "timestamp": timestamp}
    except (IndexError, KeyError):
        return JSONResponse(status_code=404, content=create_message("Circuits not found"))

    return circuits


@router.get("/circuits/{season}",
            tags=["Season"],
            response_model=Circuits,
            responses={
                404: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Circuits not found")
                    }
                }},
                200: {"model": Circuits, "content": {
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
    data, timestamp = get_cache(f"http://185.229.22.110/api/f1/{season}/circuits.json?limit=100",
                                f"get_circuits_by_season.{season}")

    try:
        circuits = {"circuits": data["MRData"]["CircuitTable"]["Circuits"], "timestamp": timestamp}
    except (IndexError, KeyError):
        return JSONResponse(status_code=404, content=create_message("Circuits not found"))

    return circuits


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
    data, timestamp = get_cache(f"http://185.229.22.110/api/f1/circuits/{circuit_id}.json",
                                f"get_circuit_by_id.{circuit_id}")

    try:
        circuit = data["MRData"]["CircuitTable"]["Circuits"][0]
        circuit["timestamp"] = timestamp
    except (IndexError, KeyError):
        return JSONResponse(status_code=404, content=create_message("Circuit not found"))

    return circuit
