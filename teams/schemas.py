from datetime import date

from pydantic import BaseModel, ConfigDict


class TeamBase(BaseModel):
    name: str


class TeamCreate(TeamBase):
    pass


class TeamUpdate(TeamCreate):
    pass


class Team(TeamCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
