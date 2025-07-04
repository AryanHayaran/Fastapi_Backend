from sqlmodel import SQLModel, text, create_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker


async_engine =  AsyncEngine(create_engine(
    url=Config.DATABASE_URL,
    # echo=True
))

async def init_db():
    async with async_engine.begin() as conn:
        from src.db.models import Book 
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() ->AsyncSession:
    Session = sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )
    async with Session() as session:
        yield session