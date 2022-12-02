from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from fastapi.routing import APIRoute

from app.routers import constructors, calendar, drivers, circuits, results, general

app = FastAPI()

load_dotenv()

# Include routers
app.include_router(calendar.router)
app.include_router(circuits.router)
app.include_router(constructors.router)
app.include_router(drivers.router)
app.include_router(results.router)
app.include_router(general.router)

# Allow all origins
origins = ["*"]

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])


# CUSTOMIZE OPENAPI
# https://fastapi.tiangolo.com/advanced/extending-openapi/

def custom_openapi():  # pragma: no coverage
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="F1 API",
        version="1.7.1",
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
