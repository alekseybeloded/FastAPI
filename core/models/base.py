import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    name: Mapped[str]
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime())
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime())

    id: Mapped[int] = mapped_column(primary_key=True)
