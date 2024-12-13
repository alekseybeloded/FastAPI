from datetime import date

from pydantic import BaseModel, ConfigDict


class TeamBase(BaseModel):
    name: str
    created_at: date
    updated_at: date


class TeamCreate(TeamBase):
    pass


class TeamUpdate(TeamCreate):
    pass


class Team(TeamCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
