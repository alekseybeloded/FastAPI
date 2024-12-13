from datetime import date

from pydantic import BaseModel, ConfigDict


class PlayerBase(BaseModel):
    name: str
    created_at: date
    updated_at: date


class PlayerCreate(PlayerBase):
    team_id: int


class PlayerUpdate(PlayerCreate):
    pass


class Player(PlayerCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
