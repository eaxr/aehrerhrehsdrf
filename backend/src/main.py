#!/bin/env python3

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from typing import List
from os import environ

from src.database.init import initDB


apiMain = FastAPI()
base = initDB(apiMain)

CORS_URL = environ.get('CORS_URL', 'http://127.0.0.1:4200')

apiMain.add_middleware(
    CORSMiddleware,
    allow_origins=[CORS_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from src.routes import notes
apiMain.include_router(notes.apiRouter)

@apiMain.get("/")
def home():
    return {'none': 'null'}
