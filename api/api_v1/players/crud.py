from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.players.schemas import PlayerCreate, PlayerUpdate
from core.models.player import Player as PlayerModel


async def add(
    obj: PlayerCreate,
    session: AsyncSession,
) -> PlayerModel:
    obj_model = PlayerModel(**obj.model_dump())

    session.add(obj_model)
    await session.commit()

    return obj_model


async def get_all(session: AsyncSession) -> list[PlayerModel]:
    stmt = select(PlayerModel).order_by(PlayerModel.id)
    result: Result = await session.execute(stmt)
    return list(result.scalars().all())


async def get_by_id(
    obj_id: int,
    session: AsyncSession
) -> PlayerModel | None:
    obj_model = await session.get(PlayerModel, obj_id)
    if not obj_model:
        raise HTTPException(status_code=404, detail="This id doesn't exist")


async def update(
    obj_id: int,
    obj_update: PlayerUpdate,
    session: AsyncSession,
) -> PlayerModel | None:
    obj_model = await session.get(PlayerModel, obj_id)
    if not obj_model:
        raise HTTPException(status_code=404, detail="This id doesn't exist")

    for name, value in obj_update.model_dump().items():
        setattr(obj_model, name, value)

    await session.commit()

    return obj_model


async def delete(
    obj_id: int,
    session: AsyncSession,
) -> None:
    obj_model = await session.get(PlayerModel, obj_id)
    if not obj_model:
        raise HTTPException(status_code=404, detail="This id doesn't exist")

    await session.delete(obj_model)
    await session.commit()
