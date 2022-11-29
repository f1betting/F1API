from starlette.responses import JSONResponse

from app.internal.models.general.message import create_message


def service_unavailable():
    return JSONResponse(status_code=503, content=create_message("Service unavailable"))


def data_not_found(msg):
    return JSONResponse(status_code=404, content=create_message(f"{msg} not found"))
