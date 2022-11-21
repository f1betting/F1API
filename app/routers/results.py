from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.internal.logic.cache_init import get_cache
from app.internal.models.f1.constructor_standing import ConstructorStandings, ConstructorStandingsExample
from app.internal.models.f1.driver_standing import DriverStandings, DriverStandingsExample
from app.internal.models.f1.qualifying_result import QualifyingResults, QualifyingResultExample
from app.internal.models.f1.race_result import RaceResults, RaceResultExample
from app.internal.models.general.message import Message, create_message

router = APIRouter(
    prefix="/results",
    tags=["Results"],
)


# RACE RESULTS
# http://185.229.22.110/mrd/methods/results/

@router.get("/race/{season}/{race}",
            response_model=RaceResults,
            responses={
                404: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Race results not found")
                    }
                }},
                503: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Service unavailable")
                    }
                }},
                200: {"model": RaceResults, "content": {
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
    data, timestamp = get_cache(f"http://185.229.22.110/api/f1/{season}/{race}/results.json",
                                f"get_race_results.{season}.{race}")

    try:
        results = {"results": data["MRData"]["RaceTable"]["Races"][0]["Results"],
                   "timestamp": timestamp}
    except IndexError:
        return JSONResponse(status_code=404, content=create_message("Race results not found"))
    except KeyError:
        return JSONResponse(status_code=503, content=create_message("Service unavailable"))

    return results


# QUALIFYING RESULTS
# http://185.229.22.110/mrd/methods/qualifying/

@router.get("/qualifying/{season}/{race}",
            response_model=QualifyingResults,
            responses={
                404: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Qualifying results not found")
                    }
                }},
                503: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Service unavailable")
                    }
                }},
                200: {"model": QualifyingResults, "content": {
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
    data, timestamp = get_cache(f"http://185.229.22.110/api/f1/{season}/{race}/qualifying.json",
                                f"get_qualifying_results.{season}.{race}")

    try:
        results = {"results": data["MRData"]["RaceTable"]["Races"][0]["QualifyingResults"],
                   "timestamp": timestamp}
    except IndexError:
        return JSONResponse(status_code=404, content=create_message("Qualifying results not found"))
    except KeyError:
        return JSONResponse(status_code=503, content=create_message("Service unavailable"))

    return results


# STANDINGS
# http://185.229.22.110/mrd/methods/standings/

@router.get("/standings/drivers/{season}",
            tags=["Season"],
            response_model=DriverStandings,
            responses={
                404: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Standings not found")
                    }
                }},
                503: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Service unavailable")
                    }
                }},
                200: {"model": DriverStandings, "content": {
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
    data, timestamp = get_cache(f"http://185.229.22.110/api/f1/{season}/driverStandings.json",
                                f"get_driver_standings_by_season.{season}")

    try:
        standings = {"standings": data["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"],
                     "timestamp": timestamp}
    except IndexError:
        return JSONResponse(status_code=404, content=create_message("Standings not found"))
    except KeyError:
        return JSONResponse(status_code=503, content=create_message("Service unavailable"))

    return standings


@router.get("/standings/constructors/{season}",
            tags=["Season"],
            response_model=ConstructorStandings,
            responses={
                404: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Standings not found")
                    }
                }},
                503: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Service unavailable")
                    }
                }},
                200: {"model": ConstructorStandings, "content": {
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
    data, timestamp = get_cache(f"http://185.229.22.110/api/f1/{season}/constructorStandings.json",
                                f"get_constructor_standings_by_season.{season}")

    try:
        standings = {"standings": data["MRData"]["StandingsTable"]["StandingsLists"][0]["ConstructorStandings"],
                     "timestamp": timestamp}
    except IndexError:
        return JSONResponse(status_code=404, content=create_message("Standings not found"))
    except KeyError:
        return JSONResponse(status_code=503, content=create_message("Service unavailable"))

    return standings
