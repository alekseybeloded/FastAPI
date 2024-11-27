from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from core.models.base import Base

if TYPE_CHECKING:
    from core.models.player import Player


class Team(Base):
    __tablename__ = "teams"

    players: Mapped[list["Player"]] = relationship(back_populates="team")
