from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base
from core.models.injury import Injury
from core.models.mixins.name import NameMixin
from core.models.mixins.timestamp import TimestampMixin

if TYPE_CHECKING:
    from core.models.team import Team


class Player(
    NameMixin,
    TimestampMixin,
    Base,
):

    team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"))

    team: Mapped["Team"] = relationship(
        back_populates="players",
        lazy="joined",
    )
    injury: Mapped["Injury"] = relationship(
        back_populates="player",
        uselist=False,
    )
