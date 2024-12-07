from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.base import Base

if TYPE_CHECKING:
    from core.models.player import Player


class Injury(Base):

    player_id: Mapped[int] = mapped_column(ForeignKey("players.id"), unique=True)

    player: Mapped["Player"] = relationship(
        back_populates="injury",
        uselist=False,
        lazy="joined",
    )
