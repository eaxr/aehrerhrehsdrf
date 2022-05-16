from fastapi import APIRouter
from fastapi import Depends
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.base import getSession
from src.database.models.notes import Notes
from src.schemas.notes import NotesCreate, NotesShow
import src.database.crud.notes as crudNotes


apiRouter = APIRouter()

@apiRouter.get('/notes', response_model=List[NotesShow])
async def getNotes(session: AsyncSession = Depends(getSession)):
    return await crudNotes.getNotes(session)

@apiRouter.post("/notes")
async def addNote(note: NotesCreate, session: AsyncSession = Depends(getSession)):
    crudNotes.addNote(note, session)
    await session.commit()
