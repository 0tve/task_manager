from sqlalchemy.ext import asyncio as sa_asyncio

from src.entities.schemas import db

async_engine = sa_asyncio.create_async_engine(db.db_credentials.URL)
async_sessionmaker = sa_asyncio.async_sessionmaker(
    async_engine, expire_on_commit=False)
