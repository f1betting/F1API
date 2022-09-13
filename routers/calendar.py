import requests
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from classes.event import Event, CalendarExample
from classes.message import Message

router = APIRouter(
    prefix="/calendar",
)


# CALENDAR
# https://ergast.com/mrd/methods/schedule/

@router.get("/{season}",
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
