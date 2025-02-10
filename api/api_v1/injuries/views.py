from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.injuries import crud
from api.api_v1.injuries.schemas import InjuryCreate, InjuryRead, InjuryUpdate
from core.models import db_helper
from fastapi import APIRouter, Depends, status, HTTPException

router = APIRouter()


@router.post(
    "/",
    response_model=InjuryRead,
    status_code=status.HTTP_201_CREATED,
)
async def add_injury(
    injury: InjuryCreate,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_dependency),
    ],
) -> InjuryRead:
    injury_model = await crud.add(obj=injury, session=session)
    return InjuryRead.model_validate(injury_model)


@router.get(
    "{injury_id}/",
    response_model=InjuryRead,
)
async def get_injury(
    injury_id: int,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_dependency),
    ],
) -> InjuryRead:
    injury_model = await crud.get_by_id(obj_id=injury_id, session=session)
    if not injury_model:
        raise HTTPException(status_code=404, detail="This id doesn't exist")
    return InjuryRead.model_validate(injury_model)


@router.get(
    "/",
    response_model=list[InjuryRead],
)
async def get_injuries(
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
    injury_update: InjuryUpdate,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_dependency),
    ],
) -> InjuryRead:
    updated_injury_model = await crud.update(
        obj_id=injury_id,
        obj_update=injury_update,
        session=session
    )
    if not updated_injury_model:
        raise HTTPException(status_code=404, detail="This id doesn't exist")
    return InjuryRead.model_validate(updated_injury_model)


@router.delete(
    "{injury_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_injury(
    injury_id: int,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_dependency),
    ],
) -> None:
    await crud.delete(obj_id=injury_id, session=session)
