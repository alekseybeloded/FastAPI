import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column


class BaseFieldsMixin:
    name: Mapped[str]
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime())
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(),
        default=datetime.datetime.now(datetime.UTC),
        onupdate=datetime.datetime.now(datetime.UTC),
    )
