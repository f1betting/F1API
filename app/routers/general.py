from fastapi import APIRouter

from app.internal.logic.cache_init import get_cache

router = APIRouter()


@router.get("/test")
def test():
    data, timestamp = get_cache("https://sandbox.api.service.nhs.uk/hello-world/hello/world", "test")
    return data
