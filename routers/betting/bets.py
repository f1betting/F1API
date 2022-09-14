from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

import main
from classes.betting.bet import BetExample, BaseBet, FullBet
from classes.general.message import Message, create_message

router = APIRouter(
    tags=["Bet"],
)


@router.get("/{username}/{race}",
            response_model=Message,
            responses={
                404: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("User not found"),
                    }
                }},
                200: {"model": FullBet, "content": {
                    "application/json": {
                        "example": BetExample
                    }
                }},
            })
def get_bet(username: str, race: int):
    user = main.app.database["Users"].find_one({"username": username.lower()})

    if not user:
        return JSONResponse(status_code=404, content=create_message("User not found"))

    bet = main.app.database["Bets"].find_one({"user": user, "round": race})

    if not bet:
        return JSONResponse(status_code=404, content=create_message("Bet not found"))

    return bet


@router.post("/",
             response_model=FullBet,
             responses={
                 404: {"model": Message, "content": {
                     "application/json": {
                         "example": create_message("User not found")
                     }
                 }},
                 409: {"model": Message, "content": {
                     "application/json": {
                         "example": create_message("Bet already exists")
                     }
                 }},
                 200: {"model": FullBet, "content": {
                     "application/json": {
                         "example": BetExample
                     }
                 }}
             })
def create_bet(bet: BaseBet):
    bet.username = bet.username.lower()
    bet.p1 = bet.p1.upper()
    bet.p2 = bet.p2.upper()
    bet.p3 = bet.p3.upper()

    bet = jsonable_encoder(bet)

    user = main.app.database["Users"].find_one({"username": bet["username"]})

    if not user:
        return JSONResponse(status_code=404, content=create_message("User not found"))

    del bet["username"]

    bet["user"] = user

    if list(main.app.database["Bets"].find({"user": bet["user"], "round": bet["round"]})):
        return JSONResponse(status_code=409, content=create_message("Bet already exists"))

    new_bet = main.app.database["Bets"].insert_one(bet)

    created_bet = main.app.database["Bets"].find_one({"_id": new_bet.inserted_id})

    return created_bet


@router.put("/{username}/{race}",
            response_model=Message,
            responses={
                404: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("User not found"),
                    }
                }},
                200: {"model": Message, "content": {
                    "application/json": {
                        "example": create_message("Bet updated succesfully")
                    }
                }},
            })
def edit_bet(username: str, race: int, p1: str, p2: str, p3: str):
    user = main.app.database["Users"].find_one({"username": username.lower()})

    if not user:
        return JSONResponse(status_code=404, content=create_message("User not found"))

    bet = main.app.database["Bets"].find_one({"user": user, "round": race})

    if not bet:
        return JSONResponse(status_code=404, content=create_message("Bet not found"))

    main.app.database["Bets"].update_one({"_id": bet["_id"]}, {"$set": {
        "p1": p1.upper(),
        "p2": p2.upper(),
        "p3": p3.upper()
    }})

    return create_message("Bet updated succesfully")


@router.delete("/{username}/{race}",
               response_model=Message,
               responses={
                   404: {"model": Message, "content": {
                       "application/json": {
                           "example": create_message("User not found")

                       }
                   }},
                   200: {"model": Message, "content": {
                       "application/json": {
                           "example": create_message("Bet deleted succesfully")
                       }
                   }},
               })
def delete_bet(username: str, race: int):
    user = main.app.database["Users"].find_one({"username": username.lower()})

    if not user:
        return JSONResponse(status_code=404, content=create_message("User not found"))

    bet = main.app.database["Bets"].find_one({"user": user, "round": race})

    if not bet:
        return JSONResponse(status_code=404, content=create_message("Bet not found"))

    main.app.database["Bets"].delete_one({"_id": bet["_id"]})

    return create_message("Bet deleted succesfully")
