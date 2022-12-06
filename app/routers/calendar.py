import os

from fastapi import APIRouter

from app.internal.logic.cache_init import get_cache, invalidate_cache
from app.internal.logic.errors import service_unavailable, data_not_found
from app.internal.models.f1.event import Calendar, EventExample, NextEvent, NextEventExample, Event, CalendarExample, \
    PreviousEventExample
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
                        "example": CalendarExample
                    }
                }}
            })
def get_calendar_by_season(season: int):
    data, timestamp = get_cache(f"{os.getenv('ERGAST_API')}/api/f1/{season}.json", f"get_calendar_by_season.{season}")

    try:
        if len(data["MRData"]["RaceTable"]["Races"]) <= 0:
            raise IndexError

        calendar = {"events": data["MRData"]["RaceTable"]["Races"], "timestamp": timestamp}
    except IndexError:
        invalidate_cache(f"get_calendar_by_season.{season}")
        return data_not_found("Calendar")
    except KeyError:
        invalidate_cache(f"get_calendar_by_season.{season}")
        return service_unavailable()

    return calendar


@router.get("/event/next",
            tags=["Events"],
            response_model=NextEvent,
            responses={
                503: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Service unavailable")
                    }
                }},
                200: {"model": NextEvent, "content": {
                    "application/json": {
                        "example": NextEventExample
                    }
                }}
            })
def get_next_race():
    data, timestamp = get_cache(f"{os.getenv('ERGAST_API')}/api/f1/current/next.json", "get_next_race")

    try:
        event_data = data["MRData"]["RaceTable"]
        event_data["timestamp"] = timestamp
    except (KeyError, IndexError):
        invalidate_cache("get_next_race")
        return service_unavailable()

    return event_data


@router.get("/event/previous",
            tags=["Events"],
            response_model=NextEvent,
            responses={
                503: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Service unavailable")
                    }
                }},
                200: {"model": NextEvent, "content": {
                    "application/json": {
                        "example": PreviousEventExample
                    }
                }}
            })
def get_previous_race():
    data, timestamp = get_cache(f"{os.getenv('ERGAST_API')}/api/f1/current/last.json", "get_previous_race")

    try:
        event_data = data["MRData"]["RaceTable"]
        event_data["timestamp"] = timestamp
    except (KeyError, IndexError):
        invalidate_cache("get_previous_race")
        return service_unavailable()

    return event_data


@router.get("/event/{season}/{race}",
            tags=["Events"],
            response_model=Event,
            responses={
                404: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Event not found")
                    }
                }},
                503: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Service unavailable")
                    }
                }},
                200: {"model": Event, "content": {
                    "application/json": {
                        "example": EventExample
                    }
                }}
            })
def get_event_details(season: int, race: int):
    data, timestamp = get_cache(f"{os.getenv('ERGAST_API')}/api/f1/{season}/{race}.json",
                                f"get_event_details.{season}.{race}")

    try:
        if len(data["MRData"]["RaceTable"]["Races"]) <= 0:
            raise IndexError

        event_data = data["MRData"]["RaceTable"]["Races"][0]
        event_data["timestamp"] = timestamp
    except IndexError:
        invalidate_cache(f"get_event_details.{season}.{race}")
        return data_not_found("Event")
    except KeyError:
        invalidate_cache(f"get_event_details.{season}.{race}")
        return service_unavailable()

    return event_data
