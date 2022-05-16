from typing import Optional
from pydantic import BaseModel


class NotesCreate(BaseModel):
    title: str
    description : str

class NotesShow(BaseModel):
    title: str
    description : str
    id: int

    class Config():
        orm_mode = True
