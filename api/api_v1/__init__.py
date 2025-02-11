__all__ = [
    "CrudBase"
]

from fastapi import APIRouter

from core.config import settings

from .injuries.views import router as injury_router
from .players.views import router as player_router
from .teams.views import router as team_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)
router.include_router(
    team_router,
    prefix=settings.api.v1.teams,
    tags=["Teams"],
)
router.include_router(
    player_router,
    prefix=settings.api.v1.players,
    tags=["Players"],
)
router.include_router(
    injury_router,
    prefix=settings.api.v1.injuries,
    tags=["Injuries"],
)
