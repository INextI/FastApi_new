from sqlalchemy.ext.asyncio import (
    create_async_engine, 
    async_sessionmaker, 
    async_scoped_session,
    AsyncSession,
    AsyncEngine
    )
from typing import AsyncGenerator
from asyncio import current_task
from core.config import settings

class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine: AsyncEngine = create_async_engine(
            url = url,
            echo = echo, 
        )
        self.session_factory = async_sessionmaker(
            bind= self.engine,
            autoflush= False,
            autocommit = False,
            expire_on_commit= False,
        )

    async def dispose(self) -> None:
        await self.engine.dispose()

    async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session

db_helper = DatabaseHelper(url= settings.db_url, echo= settings.db_echo)