from sqlalchemy.orm import Mapped, relationship

from core.models import Base
from core.models.mixins.name import NameMixin
from core.models.mixins.timestamp import TimestampMixin
from core.models.player import Player


class Team(
    NameMixin,
    TimestampMixin,
    Base,
):

    players: Mapped[list["Player"]] = relationship(
        back_populates="team",
        cascade="all, delete-orphan",
    )
