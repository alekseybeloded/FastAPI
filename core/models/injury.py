from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.base import Base
from core.models.mixins import BaseFieldsMixin

if TYPE_CHECKING:
    from core.models.player import Player


class Injury(BaseFieldsMixin, Base):

    player_id: Mapped[int] = mapped_column(ForeignKey("players.id"), unique=True)

    player: Mapped["Player"] = relationship(back_populates="injury")
