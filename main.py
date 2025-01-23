from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api import router as api_router
from core.models import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator:
    # startup
    yield
    # shutdown
    await db_helper.dispose()


main_app = FastAPI(
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)
main_app.include_router(api_router)
