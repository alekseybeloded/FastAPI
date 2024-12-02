import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    declared_attr,
    mapped_column,
    scoped_session,
    sessionmaker,
)

load_dotenv()


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primary_key=True)


db_url = os.getenv('DB_URL')
if db_url is None:
    raise ValueError("Database URL cannot be None")

engine = create_engine(db_url, echo=False)
db_session = scoped_session(sessionmaker(bind=engine))
