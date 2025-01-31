from typing import Generic, TypeVar

from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.players.schemas import PlayerCreate, PlayerUpdate
from core.models import Base
from core.models.player import Player as PlayerModel

TModel = TypeVar("TModel", bound=Base)
TCreateSchema = TypeVar("TCreateSchema", bound=BaseModel)
TUpdateSchema = TypeVar("TUpdateSchema", bound=BaseModel)


class CrudBase(Generic[TModel, TCreateSchema, TUpdateSchema]):
    def __init__(self, model: type[TModel]) -> None:
        self.model = model

    async def add(self,
        obj: TCreateSchema,
        session: AsyncSession,
    ) -> PlayerModel:
        obj_model = PlayerModel(**obj.model_dump())

        session.add(obj_model)
        await session.commit()

        return obj_model

    async def get_all(self, session: AsyncSession) -> list[TModel]:
        stmt = select(self.model).order_by(self.model.id)
        result: Result = await session.execute(stmt)
        return list(result.scalars().all())

    async def get_by_id(
        self,
        obj_id: int,
        session: AsyncSession
    ) -> TModel | None:
        return await session.get(self.model, obj_id)

    async def update(
        self,
        obj_update: TUpdateSchema,
        obj: TModel,
        session: AsyncSession,
    ) -> TModel:
        for name, value in obj_update.model_dump().items():
            setattr(obj, name, value)

        await session.commit()

        return obj

    async def delete(
        self,
        obj: TModel,
        session: AsyncSession,
    ) -> None:
        await session.delete(obj)
        await session.commit()
