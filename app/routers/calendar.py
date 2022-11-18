from json import JSONDecodeError

import requests
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.internal.logic.cache_init import cache_init, cache_write, get_cache
from app.internal.models.f1.event import Calendar, EventExample, NextEvent, NextEventExample, Event
from app.internal.models.general.message import Message, create_message

router = APIRouter()


# CALENDAR
# http://185.229.22.110/mrd/methods/schedule/

@router.get("/calendar/{season}",
            tags=["Season"],
            response_model=Calendar,
            responses={
                404: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Calendar not found")
                    }
                }},
                200: {"model": Calendar, "content": {
                    "application/json": {
                        "example": {
                            "events": [
                                EventExample
                            ]
                        }
                    }
                }}
            })
def get_calendar_by_season(season: int):
    data, timestamp = get_cache(f"http://185.229.22.110/api/f1/{season}.json", f"get_calendar_by_season.{season}")

    calendar = {"events": data["MRData"]["RaceTable"]["Races"], "timestamp": timestamp}

    if not calendar["events"]:
        return JSONResponse(status_code=404, content=create_message("Calendar not found"))

    return calendar


@router.get("/event/next",
            tags=["Events"],
            response_model=NextEvent,
            responses={
                404: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Event not found")
                    }
                }},
                200: {"model": NextEvent, "content": {
                    "application/json": {
                        "example": NextEventExample
                    }
                }}
            })
def get_next_race():
    data, timestamp = get_cache("http://185.229.22.110/api/f1/current/next.json", "get_next_race")

    event_data = data["MRData"]["RaceTable"]
    event_data["timestamp"] = timestamp

    if not event_data:
        return JSONResponse(status_code=404, content=create_message("Event not found"))

    return event_data


@router.get("/event/{season}/{round}",
            tags=["Events"],
            response_model=Event,
            responses={
                404: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Event not found")
                    }
                }},
                200: {"model": Event, "content": {
                    "application/json": {
                        "example": EventExample
                    }
                }}
            })
def get_event_details(season: int, round: int):
    data, timestamp = get_cache(f"http://185.229.22.110/api/f1/{season}/{round}.json", f"get_event_details.{season}.{round}")

    event_data = data["MRData"]["RaceTable"]["Races"][0]
    event_data["timestamp"] = timestamp

    if not event_data:
        return JSONResponse(status_code=404, content=create_message("Event not found"))

    return event_data


@router.get("/test")
def test():
    data = get_cache("https://sandbox.api.service.nhs.uk/hello-world/hello/world", "test")
    return data
