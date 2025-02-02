from pydantic import BaseModel, ConfigDict


class PlayerBase(BaseModel):
    name: str


class PlayerCreate(PlayerBase):
    team_id: int


class PlayerUpdate(PlayerCreate):
    pass


class PlayerRead(PlayerCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
