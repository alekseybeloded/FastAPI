from typing import Generic

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.constants import TCreateSchema, TModelCrud, TUpdateSchema
from api.api_v1.injuries.schemas import InjuryCreate, InjuryUpdate
from api.api_v1.players.schemas import PlayerCreate, PlayerUpdate
from api.api_v1.teams.schemas import TeamCreate, TeamUpdate
from core.models.injury import Injury as InjuryModel
from core.models.player import Player as PlayerModel
from core.models.team import Team as TeamModel


class CrudBase(Generic[TModelCrud, TCreateSchema, TUpdateSchema]):
    def __init__(self, model: type[TModelCrud]) -> None:
        self.model = model

    async def add(self,
        obj: TCreateSchema,
        session: AsyncSession,
    ) -> TModelCrud:
        obj_model = TeamModel(**obj.model_dump())

        session.add(obj_model)
        await session.commit()

        return obj_model

    async def get_all(self, session: AsyncSession) -> list[TModelCrud]:
        stmt = select(self.model).order_by(self.model.id)
        result: Result = await session.execute(stmt)
        return list(result.scalars().all())

    async def get_by_id(
        self,
        obj_id: int,
        session: AsyncSession
    ) -> TModelCrud | None:
        return await session.get(self.model, obj_id)

    async def update(
        self,
        obj_update: TUpdateSchema,
        obj: TModelCrud,
        session: AsyncSession,
    ) -> TModelCrud:
        for name, value in obj_update.model_dump().items():
            setattr(obj, name, value)

        await session.commit()

        return obj

    async def delete(
        self,
        obj: TModelCrud,
        session: AsyncSession,
    ) -> None:
        await session.delete(obj)
        await session.commit()


team_crud = CrudBase[TeamModel, TeamCreate, TeamUpdate](TeamModel)
player_crud = CrudBase[PlayerModel, PlayerCreate, PlayerUpdate](PlayerModel)
injury_crud = CrudBase[InjuryModel, InjuryCreate, InjuryUpdate](InjuryModel)
