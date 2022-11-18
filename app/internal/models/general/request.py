from pydantic import BaseModel


class BaseRequest(BaseModel):
    timestamp: float | None
