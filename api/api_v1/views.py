from typing import Annotated, Generic

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1 import CrudBase
from api.api_v1.constants import TCreateSchema, TModelCrud, TModelViews, TReadSchema, TUpdateSchema
from api.api_v1.players.schemas import PlayerRead
from api.api_v1.teams.schemas import TeamRead
from core.models import db_helper


class ViewsBase(Generic[TModelViews, TCreateSchema, TReadSchema, TUpdateSchema]):
    def __init__(
        self,
        model: type[TModelCrud],
        crud: CrudBase[TModelCrud, TCreateSchema, TUpdateSchema],
        read_schema: type[TReadSchema],
        create_schema: type[TCreateSchema],
        update_schema: type[TUpdateSchema],
    ) -> None:
        self.model = model
        self.crud = crud
        self.read_schema = read_schema
        self.create_schema = create_schema
        self.update_schema = update_schema
        self.router: APIRouter = APIRouter()

        self.add_routes()

    def add_routes(self) -> None:
        self.router.get(
            "/",
            response_model=list[TeamRead | PlayerRead],
        )(self.get_all)
        self.router.get(
            "/{item_id}/",
            response_model=TeamRead | PlayerRead,
        )(self.get_by_id)
        self.router.post(
            "/",
            response_model=TeamRead | PlayerRead,
            status_code=status.HTTP_201_CREATED,
        )(self.create)
        self.router.put(
            "/{item_id}/",
            response_model=TeamRead | PlayerRead,
        )(self.update)
        self.router.delete(
            "/{item_id}/",
            status_code=status.HTTP_204_NO_CONTENT,
        )(self.delete)

    async def get_all(
        self,
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_dependency),
        ]
    ) -> list[TReadSchema]:
        items = await self.crud.get_all(session=session)
        return [self.read_schema.model_validate(item) for item in items]

    async def get_by_id(
        self,
        item_id: int,
        session: Annotated[AsyncSession, Depends(db_helper.session_dependency)],
    ) -> TReadSchema | None:
        item = await self.crud.get_by_id(obj_id=item_id, session=session)
        return self.read_schema.model_validate(item)

    async def create(
        self,
        item: TCreateSchema,
        session: Annotated[AsyncSession, Depends(db_helper.session_dependency)],
    ) -> TReadSchema:
        created_item: TModelCrud = await self.crud.add(
            obj=item,
            session=session,
        )
        return self.read_schema.model_validate(created_item)

    async def update(
        self,
        item_update: TUpdateSchema,
        item: TModelViews,
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_dependency)
        ],
    ) -> TReadSchema:
        item = await self.crud.update(
            obj_update=item_update,
            obj=item,
            session=session,
        )
        return self.read_schema.model_validate(item)

    async def delete(
        self,
        item: TModelViews,
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_dependency)
        ],
    ) -> None:
        await self.crud.delete(
            obj=item,
            session=session,
        )
