from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship

from core.models import Base
from core.models.mixins.name import NameMixin
from core.models.mixins.timestamp import TimestampMixin

if TYPE_CHECKING:
    from core.models.player import Player


class Injury(
    NameMixin,
    TimestampMixin,
    Base,
):
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return "injuries"

    player_id: Mapped[int] = mapped_column(ForeignKey("players.id"), unique=True)

    player: Mapped["Player"] = relationship(
        back_populates="injury",
        uselist=False,
        lazy="joined",
    )
