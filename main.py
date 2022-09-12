from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse
from fastapi.routing import APIRoute

from Classes.Constructor import ConstructorExample, Constructor
from Classes.Driver import Driver, DriverExample
from Classes.Event import Event, CalendarExample
from Classes.Circuit import Circuit, CircuitExample
from Classes.Message import Message
from Classes.QualifyingResult import QualifyingResult, QualifyingResultExample
from Classes.RaceResult import RaceResult, RaceResultExample
from Classes.Standing import Standing, StandingsExample

import requests

app = FastAPI()


# RACE RESULTS
# https://ergast.com/mrd/methods/results/

@app.get("/results/race/{season}/{race}",
         tags=["Results"],
         response_model=list[RaceResult],
         responses={
             404: {"model": Message, "description": "Race results not found"},
             200: {"model": RaceResult, "content": {
                 "application/json": {
                     "example": [
                         RaceResultExample
                     ]
                 }
             }}
         })
async def get_race_results(season: int, race: int):
    url = f"https://ergast.com/api/f1/{season}/{race}/results.json"
    res = requests.get(url)
    data = res.json()
    race_results = data["MRData"]["RaceTable"]["Races"]

    if not race_results:
        return JSONResponse(status_code=404, content={"message": "Race results not found"})

    if race_results:
        race_results = race_results[0]["Results"]

    return race_results


# QUALIFYING RESULTS
# https://ergast.com/mrd/methods/qualifying/

@app.get("/results/qualifying/{season}/{race}",
         tags=["Results"],
         response_model=list[QualifyingResult],
         responses={
             404: {"model": Message, "description": "Qualifying results not found"},
             200: {"model": QualifyingResult, "content": {
                 "application/json": {
                     "example": [
                         QualifyingResultExample
                     ]
                 }
             }}
         })
def get_qualifying_results(season: int, race: int):
    url = f"https://ergast.com/api/f1/{season}/{race}/qualifying.json"
    res = requests.get(url)
    data = res.json()
    qualifying_results = data["MRData"]["RaceTable"]["Races"]

    if not qualifying_results:
        return JSONResponse(status_code=404, content={"message": "Qualifying results not found"})

    if qualifying_results:
        qualifying_results = qualifying_results[0]["QualifyingResults"]

    return qualifying_results


# STANDINGS
# https://ergast.com/mrd/methods/standings/

@app.get("/standings/{season}",
         tags=["Results", "Season"],
         response_model=list[Standing],
         responses={
             404: {"model": Message, "description": "Standings not found"},
             200: {"model": Standing, "content": {
                 "application/json": {
                     "example": [
                         StandingsExample
                     ]
                 }
             }}
         })
async def get_standings_by_season(season: int):
    url = f"https://ergast.com/api/f1/{season}/driverStandings.json"
    res = requests.get(url)
    data = res.json()
    standings = data["MRData"]["StandingsTable"]["StandingsLists"]

    if not standings:
        return JSONResponse(status_code=404, content={"message": "Standings not found"})

    if standings:
        standings = standings[0]["DriverStandings"]

    return standings


# CALENDAR
# https://ergast.com/mrd/methods/schedule/

@app.get("/calendar/{season}",
         tags=["Season"],
         response_model=list[Event],
         responses={
             404: {"model": Message, "description": "Calendar not found"},
             200: {"model": Event, "content": {
                 "application/json": {
                     "example": [
                         CalendarExample
                     ]
                 }
             }}
         })
async def get_calendar_by_season(season: int):
    url = f"https://ergast.com/api/f1/{season}.json"
    res = requests.get(url)
    data = res.json()
    calendar = data["MRData"]["RaceTable"]["Races"]

    if not calendar:
        return JSONResponse(status_code=404, content={"message": "Calendar not found"})

    return calendar


# CIRCUITS
# https://ergast.com/mrd/methods/circuits/

@app.get("/circuits",
         tags=["Circuits"],
         response_model=list[Circuit],
         responses={
             404: {"model": Message, "description": "Circuits not found"},
             200: {"model": Circuit, "content": {
                 "application/json": {
                     "example": [
                         CircuitExample
                     ]
                 }
             }}
         })
async def get_circuits():
    url = f"https://ergast.com/api/f1/circuits.json?limit=100"
    res = requests.get(url)
    data = res.json()
    circuits = data["MRData"]["CircuitTable"]["Circuits"]

    if not circuits:
        return JSONResponse(status_code=404, content={"message": "Circuits not found"})

    return circuits


@app.get("/circuits/{season}",
         tags=["Circuits", "Season"],
         response_model=list[Circuit],
         responses={
             404: {"model": Message, "description": "Circuits not found"},
             200: {"model": Circuit, "content": {
                 "application/json": {
                     "example": [
                         CircuitExample
                     ]
                 }
             }}
         })
async def get_circuits_by_season(season: str):
    url = f"https://ergast.com/api/f1/{season}/circuits.json?limit=100"
    res = requests.get(url)
    data = res.json()
    circuits = data["MRData"]["CircuitTable"]["Circuits"]

    if not circuits:
        return JSONResponse(status_code=404, content={"message": "Circuits not found"})

    return circuits


@app.get("/circuit/{circuit_id}",
         tags=["Circuits"],
         response_model=Circuit,
         responses={
             404: {"model": Message, "description": "Circuit not found"},
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
        return JSONResponse(status_code=404, content={"message": "Circuit not found"})

    return circuit[0]


# DRIVERS
# https://ergast.com/mrd/methods/drivers/

@app.get("/drivers",
         tags=["Drivers"],
         response_model=list[Driver],
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


@app.get("/drivers/{season}",
         tags=["Drivers", "Season"],
         response_model=list[Driver],
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


@app.get("/driver/{driver_id}",
         tags=["Drivers"],
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


# CONSTRUCTORS
# https://ergast.com/mrd/methods/constructors/

@app.get("/constructors",
         tags=["Constructors"],
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


@app.get("/constructors/{season}",
         tags=["Constructors", "Season"],
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


@app.get("/constructor/{constructor_id}",
         tags=["Constructors"],
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


# CUSTOMIZE OPENAPI
# https://fastapi.tiangolo.com/advanced/extending-openapi/

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="F1 API",
        version="1.0.0",
        description="An easier way to use the [ergast.com]() F1 API, with correct types!",
        routes=app.routes,
    )

    openapi_schema["info"]["x-logo"] = {
        "url": "https://upload.wikimedia.org/wikipedia/commons/f/f2/New_era_F1_logo.png"
    }

    app.openapi_schema = openapi_schema

    return app.openapi_schema


# SET FUNCTION NAME AS OPERATION ID
# https://fastapi.tiangolo.com/advanced/path-operation-advanced-configuration/#using-the-path-operation-function-name-as-the-operationid

def function_name_as_operation_id(fast_api: FastAPI):
    for route in fast_api.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name


function_name_as_operation_id(app)

app.openapi = custom_openapi
