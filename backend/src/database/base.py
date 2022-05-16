from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.engine import engine


asyncSession = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

async def getSession() -> AsyncSession:
    async with asyncSession() as session:
        yield session
