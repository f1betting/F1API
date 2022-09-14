import requests
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from classes.f1.constructor_standing import ConstructorStanding, ConstructorStandings, ConstructorStandingsExample
from classes.f1.driver_standing import DriverStanding, DriverStandings, DriverStandingsExample
from classes.general.message import Message, create_message
from classes.f1.qualifying_result import QualifyingResult, QualifyingResults, QualifyingResultExample
from classes.f1.race_result import RaceResult, RaceResults, RaceResultExample

router = APIRouter(
    prefix="/results",
    tags=["Results"],
)


# RACE RESULTS
# https://ergast.com/mrd/methods/results/

@router.get("/race/{season}/{race}",
            response_model=list[RaceResult],
            responses={
                404: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Race results not found")
                    }
                }},
                200: {"model": RaceResult, "content": {
                    "application/json": {
                        "example": {
                            "results": [
                                RaceResultExample
                            ]
                        }
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

    return {"results": race_results}


# QUALIFYING RESULTS
# https://ergast.com/mrd/methods/qualifying/

@router.get("/qualifying/{season}/{race}",
            response_model=QualifyingResults,
            responses={
                404: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Qualifying results not found")
                    }
                }},
                200: {"model": QualifyingResult, "content": {
                    "application/json": {
                        "example": {
                            "results": [
                                QualifyingResultExample
                            ]
                        }
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

    return {"results": qualifying_results}


# STANDINGS
# https://ergast.com/mrd/methods/standings/

@router.get("/standings/drivers/{season}",
            tags=["Season"],
            response_model=DriverStandings,
            responses={
                404: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Standings not found")
                    }
                }},
                200: {"model": DriverStanding, "content": {
                    "application/json": {
                        "example": {
                            "standings": [
                                DriverStandingsExample
                            ]
                        }
                    }
                }}
            })
def get_driver_standings_by_season(season: int):
    url = f"https://ergast.com/api/f1/{season}/driverStandings.json"
    res = requests.get(url)
    data = res.json()
    standings = data["MRData"]["StandingsTable"]["StandingsLists"]

    if not standings:
        return JSONResponse(status_code=404, content={"message": "Standings not found"})

    if standings:
        standings = standings[0]["DriverStandings"]

    return {"standings": standings}


@router.get("/standings/constructors/{season}",
            tags=["Season"],
            response_model=ConstructorStandings,
            responses={
                404: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Standings not found")
                    }
                }},
                200: {"model": ConstructorStanding, "content": {
                    "application/json": {
                        "example": {
                            "standings": [
                                ConstructorStandingsExample
                            ]
                        }
                    }
                }}
            })
def get_constructor_standings_by_season(season: int):
    url = f"https://ergast.com/api/f1/{season}/constructorStandings.json"
    res = requests.get(url)
    data = res.json()
    standings = data["MRData"]["StandingsTable"]["StandingsLists"]

    if not standings:
        return JSONResponse(status_code=404, content={"message": "Standings not found"})

    if standings:
        standings = standings[0]["ConstructorStandings"]

    return {"standings": standings}
