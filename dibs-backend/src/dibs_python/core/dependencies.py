from collections.abc import AsyncGenerator
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from dibs_python.core.database import get_db_session_maker
from dibs_python.core.settings import Settings, get_settings


async def get_db_transaction() -> AsyncGenerator[AsyncSession]:
    """
    Function to get database transaction.
    """
    async with get_db_session_maker()() as session, session.begin():
        yield session


# Dependency annotations

SettingsDep = Annotated[Settings, Depends(get_settings)]
DbTransactionDep = Annotated[AsyncSession, Depends(get_db_transaction)]
