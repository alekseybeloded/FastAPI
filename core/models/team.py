from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from core.models.base import Base
from core.models.mixins import BaseFieldsMixin

if TYPE_CHECKING:
    from core.models.player import Player


class Team(BaseFieldsMixin, Base):

    players: Mapped[list["Player"]] = relationship(back_populates="team")
