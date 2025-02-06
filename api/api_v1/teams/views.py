from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.crud import team_cru
from api.api_v1.teams.schemas import TeamCreate, TeamRead, TeamUpdate
from api.api_v1.views import ViewsBase
from core.models import db_helper
from core.models.team import Team as TeamModel

router = APIRouter()


@router.post(
    "/",
    response_model=TeamRead,
    status_code=status.HTTP_201_CREATED,
)
async def add_team(
    team: TeamCreate,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_dependency),
    ]
) -> TeamRead:
    team_model = await crud.add(create_item=team)
    return TeamRead.model_validate(team_model)


@router.get(
    "/",
    response_model=list[TeamRead],
)
async def get_teams(
    session: Annotated[
        AsyncSession, Depends(db_helper.session_dependency),
    ]
) -> list[TeamRead]:
    team_models = await crud.get_all(session=session)
    return [TeamRead.model_validate(team) for team in team_models]


@router.get(
    "{team_id}/",
    response_model=TeamRead,
)
async def get_team_by_id(
    team_id: int,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_dependency),
    ],
) -> TeamRead:
    team_model = await crud.get_by_id(item_id=team_id)
    return TeamRead.model_validate(team_model)


@router.put(
    "{team_id}/",
    response_model=TeamRead,
)
async def get_team(
    team_id: int,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_dependency),
    ],
) -> TeamRead:
    team_model = crud.update(
        item_id=team_id,
        session=session,
    )
    return TeamRead.model_validate(team_model)


@router.delete(
    "{team_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_team(
    team_id: int,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_dependency),
    ],
) -> None:
    await crud.delete(
        item_id=team_id,
        session=session,
    )


team_views = ViewsBase[
    TeamModel,
    TeamCreate,
    TeamRead,
    TeamUpdate,
](
    model=TeamModel,
    crud=team_crud,
    read_schema=TeamRead,
    create_schema=TeamCreate,
    update_schema=TeamUpdate,
)
