from src.database.engine import SQLALCHEMY_DATABASE_URL
from src.database.engine import Base, engine


def initDB(api) -> None:
    @api.on_event("startup")
    async def init():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

