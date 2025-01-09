from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.player import Player as PlayerModel
from players.schemas import PlayerCreate, PlayerUpdate


async def add(
    player: PlayerCreate,
    session: AsyncSession,
) -> PlayerModel:
    player_model = PlayerModel(**player.model_dump())

    session.add(player_model)
    await session.commit()

    return player_model


async def get_all(session: AsyncSession) -> list[PlayerModel]:
    stmt = select(PlayerModel).order_by(PlayerModel.id)
    result: Result = await session.execute(stmt)
    players = result.scalars().all()

    return list(players)


async def get_by_id(player_id: int, session: AsyncSession) -> PlayerModel | None:
    return await session.get(PlayerModel, player_id)


async def update(
    player_update: PlayerUpdate,
    player: PlayerModel,
    session: AsyncSession,
) -> PlayerModel:
    for name, value in player_update.model_dump().items():
        setattr(player, name, value)

    await session.commit()

    return player


async def delete(
    player: PlayerModel,
    session: AsyncSession,
) -> None:
    await session.delete(player)
    await session.commit()
