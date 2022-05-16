from os import environ

import asyncio
from sqlalchemy.ext.asyncio import create_async_engine

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE_USER = environ.get("DATABASE_USER", "username")
DATABASE_PASS = environ.get("DATABASE_PASS", "password")
DATABASE_HOST = environ.get("DATABASE_HOST", "localhost:5432")
DATABASE_NAME = environ.get("DATABASE_NAME", "test")

# backward
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DATABASE_USER}:{DATABASE_PASS}@{DATABASE_HOST}/{DATABASE_NAME}"
)
# new
SQLALCHEMY_DATABASE_ASYNC_URL = (
    f"postgresql+asyncpg://{DATABASE_USER}:{DATABASE_PASS}@{DATABASE_HOST}/{DATABASE_NAME}"
)

Base = declarative_base()
engineInit = create_engine(SQLALCHEMY_DATABASE_URL)
engine = create_async_engine(SQLALCHEMY_DATABASE_ASYNC_URL)
