import requests
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.internal.models.f1.event import Calendar, EventExample, NextEvent, NextEventExample, Event
from app.internal.models.general.message import Message, create_message

router = APIRouter()


# CALENDAR
# https://ergast.com/mrd/methods/schedule/

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
    url = f"https://ergast.com/api/f1/{season}.json"
    res = requests.get(url)
    data = res.json()
    calendar = data["MRData"]["RaceTable"]["Races"]

    if not calendar:
        return JSONResponse(status_code=404, content=create_message("Calendar not found"))

    return {"events": calendar}


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
    url = f"https://ergast.com/api/f1/current/next/results.json"
    res = requests.get(url)
    data = res.json()
    event_data = data["MRData"]["RaceTable"]

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
    url = f"https://ergast.com/api/f1/{season}/{round}.json"
    res = requests.get(url)
    data = res.json()
    event_data = data["MRData"]["RaceTable"]["Races"][0]

    if not event_data:
        return JSONResponse(status_code=404, content=create_message("Event not found"))

    return event_data
