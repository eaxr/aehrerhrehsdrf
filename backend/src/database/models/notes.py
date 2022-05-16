from sqlalchemy import Column, String
from src.database.engine import Base
from src.database.db import baseNotes


class Notes(baseNotes, Base):
    __tablename__ = 'notes'

    title = Column(String)
    description = Column(String)

    def __init__(self, title, description, created_by):
        baseNotes.__init__(self, created_by)
        self.title = title
        self.description = description
