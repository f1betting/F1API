from pydantic import BaseModel


class BaseRequest(BaseModel):
    timestamp: float | None


baseRequestExample = {
    "timestamp": 0
}
