from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.team import Team as TeamModel
from teams.schemas import TeamCreate, TeamUpdate


async def add(team: TeamCreate, session: AsyncSession, ) -> TeamModel:
    team_model = TeamModel(**team.model_dump())

    session.add(team_model)
    await session.commit()

    return team_model


async def get_all(session: AsyncSession) -> list[TeamModel]:
    stmt = select(TeamModel).order_by(TeamModel.id)
    result: Result = await session.execute(stmt)
    teams = result.scalars().all()
    return list(teams)


async def get_by_id(
    team_id: int,
    session: AsyncSession,
) -> TeamModel | None:
    return await session.get(TeamModel, team_id)


async def update(
    team_update: TeamUpdate,
    team: TeamModel,
    session: AsyncSession
) -> TeamModel:
    for name, value in team_update.model_dump().items():
        setattr(team, name, value)
    await session.commit()
    return team


async def delete(
    team: TeamModel,
    session: AsyncSession,
) -> None:
    await session.delete(team)
