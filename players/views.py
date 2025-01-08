from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.db_helper import db_helper
from core.models.player import Player as PlayerModel
from players import crud
from players.dependencies import get_player_by_id
from players.schemas import Player, PlayerCreate, PlayerUpdate

router = APIRouter(prefix="/players", tags=["Players"])


@router.get(
    "/",
    response_model=list[Player],
)
async def get_players(
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> list[PlayerModel]:
    return await crud.get_all(session=session)


@router.get(
    "/{player_id}/",
    response_model=Player
)
async def get_player(
    player: PlayerModel = Depends(get_player_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency)
) -> PlayerModel | None:
    return player


@router.post(
    "/", response_model=Player,
    status_code=status.HTTP_201_CREATED,
)
async def add_player(
    player: PlayerCreate,
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> PlayerModel:
    return await crud.add(
    player=player,
    session=session
)


@router.put("/{player_id}/", response_model=Player)
async def update_player(
    player_update: PlayerUpdate,
    player: PlayerModel = Depends(get_player_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> PlayerModel:
    return await crud.update(
        player_update=player_update,
        player=player,
        session=session,
    )


@router.delete(
    "/{player_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_player(
    player: PlayerModel = Depends(get_player_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency)
) -> None:
    await crud.delete(
        player=player,
        session=session,
    )
