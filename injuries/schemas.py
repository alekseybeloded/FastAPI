from datetime import date

from pydantic import BaseModel, ConfigDict


class InjuryBase(BaseModel):
    name: str
    created_at: date
    updated_at: date


class InjuryCreate(InjuryBase):
    player_id: int


class Injury(InjuryCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
