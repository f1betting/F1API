import os

from fastapi import APIRouter

from app.internal.logic.cache_init import get_cache, invalidate_cache
from app.internal.logic.errors import service_unavailable, data_not_found
from app.internal.models.f1.circuit import Circuit, Circuits, CircuitExample, CircuitsExample
from app.internal.models.general.message import Message, create_message

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
                503: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Service unavailable")
                    }
                }},
                200: {"model": Circuits, "content": {
                    "application/json": {
                        "example": CircuitsExample
                    }
                }}
            })
async def get_circuits():
    data, timestamp = get_cache(f"{os.getenv('ERGAST_API')}/api/f1/circuits.json?limit=100", "get_circuits")

    try:
        if len(data["MRData"]["CircuitTable"]["Circuits"]) <= 0:
            raise IndexError

        circuits = {"circuits": data["MRData"]["CircuitTable"]["Circuits"], "timestamp": timestamp}
    except IndexError:
        invalidate_cache("get_circuits")
        return data_not_found("Circuits")
    except KeyError:
        invalidate_cache("get_circuits")
        return service_unavailable()

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
                503: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Service unavailable")
                    }
                }},
                200: {"model": Circuits, "content": {
                    "application/json": {
                        "example": CircuitsExample
                    }
                }}
            })
async def get_circuits_by_season(season: str):
    data, timestamp = get_cache(f"{os.getenv('ERGAST_API')}/api/f1/{season}/circuits.json?limit=100",
                                f"get_circuits_by_season.{season}")

    try:
        if len(data["MRData"]["CircuitTable"]["Circuits"]) <= 0:
            raise IndexError

        circuits = {"circuits": data["MRData"]["CircuitTable"]["Circuits"], "timestamp": timestamp}
    except IndexError:
        invalidate_cache(f"get_circuits_by_season.{season}")
        return data_not_found("Circuits")
    except KeyError:
        invalidate_cache(f"get_circuits_by_season.{season}")
        return service_unavailable()

    return circuits


@router.get("/circuit/{circuit_id}",
            response_model=Circuit,
            responses={
                404: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Circuit not found")
                    }
                }},
                503: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Service unavailable")
                    }
                }},
                200: {"model": Circuit, "content": {
                    "application/json": {
                        "example": CircuitExample
                    }
                }}
            })
async def get_circuit_by_id(circuit_id: str):
    data, timestamp = get_cache(f"{os.getenv('ERGAST_API')}/api/f1/circuits/{circuit_id}.json",
                                f"get_circuit_by_id.{circuit_id}")

    try:
        circuit = data["MRData"]["CircuitTable"]["Circuits"][0]
        circuit["timestamp"] = timestamp
    except IndexError:
        invalidate_cache(f"get_circuit_by_id.{circuit_id}")
        return data_not_found("Circuit")
    except KeyError:
        invalidate_cache(f"get_circuit_by_id.{circuit_id}")
        return service_unavailable()

    return circuit
