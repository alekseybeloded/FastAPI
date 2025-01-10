from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
)

from core.config import settings


class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False) -> None:
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            expire_on_commit=False,
        )

    async def session_dependency(self) -> AsyncGenerator:
        async with self.session_factory() as session:
            yield session


db_helper = DatabaseHelper(
    url=settings.get_db_url(),
    echo=settings.db_echo,
)
