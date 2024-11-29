import datetime
import os

from sqlalchemy import DateTime, create_engine
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    scoped_session,
    sessionmaker,
)


class Base(DeclarativeBase):
    name: Mapped[str]
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime())
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime())

    id: Mapped[int] = mapped_column(primary_key=True)


db_url = os.environ['DB_URL']
engine = create_engine("sqlite://", echo=True)
db_session = scoped_session(sessionmaker(bind=engine))
