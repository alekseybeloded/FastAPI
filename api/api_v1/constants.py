from typing import TypeVar

from pydantic import BaseModel

from core.models.base import Base

TModelViews = TypeVar("TModelViews")
TModelCrud = TypeVar("TModelCrud", bound=Base)
TCreateSchema = TypeVar("TCreateSchema", bound=BaseModel)
TReadSchema = TypeVar("TReadSchema", bound=BaseModel)
TUpdateSchema = TypeVar("TUpdateSchema", bound=BaseModel)
