from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.players import crud
from api.api_v1.players.schemas import PlayerCreate, PlayerRead, PlayerUpdate
from core.models import db_helper
from fastapi import APIRouter, Depends, status, HTTPException

router = APIRouter()


@router.post(
    "/",
    response_model=PlayerRead,
    status_code=status.HTTP_201_CREATED,
)
async def add_player(
    player: PlayerCreate,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_dependency),
    ]
) -> PlayerRead:
    player_model = await crud.add(obj=player, session=session)
    return PlayerRead.model_validate(player_model)


@router.get(
    "/",
    response_model=list[PlayerRead],
)
async def get_players(
    session: Annotated[
        AsyncSession, Depends(db_helper.session_dependency),
    ]
) -> list[PlayerRead]:
    player_models = await crud.get_all(session=session)
    return [PlayerRead.model_validate(team) for team in player_models]


@router.get(
    "{player_id}/",
    response_model=PlayerRead,
)
async def get_player(
    player_id: int,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_dependency),
    ],
) -> PlayerRead:
    player_model = await crud.get_by_id(obj_id=player_id, session=session)
    if not player_model:
        raise HTTPException(status_code=404, detail="This id doesn't exist")
    return PlayerRead.model_validate(player_model)


@router.put(
    "{player_id}/",
    response_model=PlayerRead,
)
async def update_player(
    player_id: int,
    player_update: PlayerUpdate,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_dependency),
    ],
) -> PlayerRead:
    player_model = await crud.update(
        obj_id=player_id,
        obj_update=player_update,
        session=session,
    )
    if not player_model:
        raise HTTPException(status_code=404, detail="This id doesn't exist")
    return PlayerRead.model_validate(player_model)


@router.delete(
    "{player_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_player(
    player_id: int,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_dependency),
    ],
) -> None:
    await crud.delete(
        obj_id=player_id,
        session=session,
    )
