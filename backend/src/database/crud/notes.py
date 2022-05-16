from typing import List

import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.database.engine import engine
from src.database.base import getSession
from src.database.models.notes import Notes
from src.schemas.notes import NotesCreate


async def getNotes(session: AsyncSession):
    result = await session.execute(select(Notes))
    return result.scalars().all()

def addNote(note: NotesCreate, session: AsyncSession):
    note = Notes(title=note.title,
        description = note.description,
        created_by=""
        )

    session.add(note)
    return "done"
