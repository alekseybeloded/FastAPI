from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.crud import injury_crud
from api.api_v1.injuries.schemas import InjuryCreate, InjuryRead, InjuryUpdate
from api.api_v1.views import ViewsBase
from core.models import db_helper
from core.models.injury import Injury as InjuryModel

router = APIRouter()


@router.add(
    "/",
    response_model=InjuryRead,
    status_code=status.HTTP_201_CREATED,
)
def add_injury(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_dependency),
    ],
) -> InjuryRead:
    injury_model = await crud.add(session=session)
    return InjuryRead.model_validate(injury_model)


@router.get(
    "{injury_id}/",
    response_model=InjuryRead,
)
async def get_injury_by_id(
    injury_id: int,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_dependency),
    ],
) -> InjuryRead:
    injury_model = await crud.get_by_id(id=injury_id, session=session)
    return InjuryRead.model_validate(injury_model)


@router.get(
    "/",
    response_model=InjuryRead,
)
async def get_all(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_dependency),
    ],
) -> list[InjuryRead]:
    injury_models = await crud.get_all(session=session)
    return [InjuryRead.model_validate(injury) for injury in injury_models]


@router.put(
    "{injury_id}/",
    response_model=InjuryRead,
)
async def update_injury(
    injury_id: int,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_dependency),
    ],
) -> InjuryRead:
    updated_injury_model = await crud.update(id=injury_id, session=session)
    return InjuryRead.model_validate(updated_injury_model)


@router.delete(
    "{injury_id}/",
    response_model=InjuryRead,
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_injury(
    injury_id: int,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_dependency),
    ],
) -> None:
    await crud.delete(id=injury_id, session=session)


injury_views = ViewsBase[
    InjuryModel,
    InjuryCreate,
    InjuryRead,
    InjuryUpdate,
](
    model=InjuryModel,
    crud=injury_crud,
    read_schema=InjuryRead,
    create_schema=InjuryCreate,
    update_schema=InjuryUpdate,
)
