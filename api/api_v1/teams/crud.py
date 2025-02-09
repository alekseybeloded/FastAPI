from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.teams.schemas import TeamCreate, TeamUpdate
from core.models.team import Team as TeamModel


async def add(
    obj: TeamCreate,
    session: AsyncSession,
) -> TeamModel:
    obj_model = TeamModel(**obj.model_dump())

    session.add(obj_model)
    await session.commit()

    return obj_model


async def get_all(session: AsyncSession) -> list[TeamModel]:
    stmt = select(TeamModel).order_by(TeamModel.id)
    result: Result = await session.execute(stmt)
    return list(result.scalars().all())


async def get_by_id(
    obj_id: int,
    session: AsyncSession
) -> TeamModel | None:
    return await session.get(TeamModel, obj_id)


async def update(
    obj_id: int,
    obj_update: TeamUpdate,
    session: AsyncSession,
) -> TeamModel | None:
    obj_model = await session.get(TeamModel, obj_id)
    if obj_model is None:
        return None

    for name, value in obj_update.model_dump().items():
        setattr(obj_model, name, value)

    await session.commit()

    return obj_model


async def delete(
    obj_id: int,
    session: AsyncSession,
) -> None:
    obj_model = session.get(TeamModel, obj_id)

    await session.delete(obj_model)
    await session.commit()
