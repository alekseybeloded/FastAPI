from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.injuries.schemas import InjuryCreate, InjuryUpdate
from core.models.injury import Injury as InjuryModel


async def add(
    obj: InjuryCreate,
    session: AsyncSession,
) -> InjuryModel:
    obj_model = InjuryModel(**obj.model_dump())

    session.add(obj_model)
    await session.commit()

    return obj_model


async def get_all(session: AsyncSession) -> list[InjuryModel]:
    stmt = select(InjuryModel).order_by(InjuryModel.id)
    result: Result = await session.execute(stmt)
    return list(result.scalars().all())


async def get_by_id(
    obj_id: int,
    session: AsyncSession
) -> InjuryModel | None:
    return await session.get(InjuryModel, obj_id)


async def update(
    obj_id: int,
    obj_update: InjuryUpdate,
    session: AsyncSession,
) -> InjuryModel | None:
    obj_model = await session.get(InjuryModel, obj_id)
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
    obj_model = await session.get(InjuryModel, obj_id)

    await session.delete(obj_model)
    await session.commit()
