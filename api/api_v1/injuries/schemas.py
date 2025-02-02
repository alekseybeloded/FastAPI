from pydantic import BaseModel, ConfigDict


class InjuryBase(BaseModel):
    name: str


class InjuryCreate(InjuryBase):
    player_id: int


class InjuryUpdate(InjuryCreate):
    pass


class InjuryRead(InjuryCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
