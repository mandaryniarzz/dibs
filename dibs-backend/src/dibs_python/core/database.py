from functools import lru_cache

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from dibs_python.core.settings import get_settings


@lru_cache
def get_db_engine() -> AsyncEngine:
    """
    Function to get database engine.
    """
    settings = get_settings()
    return create_async_engine(settings.db_url, echo=settings.app_debug)


@lru_cache
def get_db_session_maker() -> async_sessionmaker[AsyncSession]:
    """
    Function to get database session maker.
    """
    engine = get_db_engine()
    return async_sessionmaker(engine, expire_on_commit=False)
