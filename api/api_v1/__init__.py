__all__ = [
    "CrudBase"
]

from fastapi import APIRouter

from core.config import settings

from .crud import CrudBase
from .injuries.views import injury_views
from .players.views import player_views
from .teams.views import team_views

router = APIRouter(
    prefix=settings.api.v1.prefix,
)
router.include_router(
    team_views.router,
    prefix=settings.api.v1.teams,
    tags=["Teams"],
)
router.include_router(
    player_views.router,
    prefix=settings.api.v1.players,
    tags=["Players"],
)
router.include_router(
    injury_views.router,
    prefix=settings.api.v1.injuries,
    tags=["Injuries"],
)
