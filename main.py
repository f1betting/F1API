from dotenv import dotenv_values
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.routing import APIRoute
from pymongo import MongoClient

from routers.betting import user, bets
from routers.f1 import constructors, results, drivers, calendar, circuits

app = FastAPI()

# Include routers
app.include_router(calendar.router, prefix="/f1")
app.include_router(circuits.router, prefix="/f1")
app.include_router(constructors.router, prefix="/f1")
app.include_router(drivers.router, prefix="/f1")
app.include_router(results.router, prefix="/f1")

app.include_router(user.router, prefix="/betting")
app.include_router(bets.router, prefix="/betting")


@app.on_event("startup")
def startup_database():
    config = dotenv_values(".env")

    app.mongodb_client = MongoClient(config["DB_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")


@app.on_event("shutdown")
def shutdown_database():
    app.mongodb_client.close()


# CUSTOMIZE OPENAPI
# https://fastapi.tiangolo.com/advanced/extending-openapi/

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="F1 API",
        version="1.0.0",
        description="An easier way to use the [ergast.com](https://ergast.com/mrd/) F1 API, with correct types!",
        license_info={
            "name": "MIT",
            "url": "https://github.com/niek-o/F1API/blob/main/LICENSE.md"
        },
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
