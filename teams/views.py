from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.db_helper import db_helper
from core.models.team import Team as TeamModel
from teams import crud
from teams.dependencies import get_team_by_id
from teams.schemas import Team, TeamCreate, TeamUpdate

router = APIRouter(prefix="/teams", tags=["Teams"])


@router.get("/", response_model=list[Team])
async def get_teams(
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> list[TeamModel]:
    return await crud.get_all(session)


@router.get("{team_id}/", response_model=Team)
async def get_team(
    team: TeamModel = Depends(get_team_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> TeamModel:
    return team


@router.post("/", response_model=Team)
async def add_team(
    team: TeamCreate,
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> TeamModel:
    return await crud.add(team, session)


@router.put("/{team_id}", response_model=Team)
async def update_team(
    team_update: TeamUpdate,
    team: TeamModel = Depends(get_team_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> TeamModel:
    return await crud.update(team_update, team, session)


@router.delete("/{team_id}")
async def delete_team(
    team: TeamModel = Depends(get_team_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency)
) -> None:
    await crud.delete(team, session)
