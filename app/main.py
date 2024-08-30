from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from . import models, crud, database

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.get('/text')
def read_text(db: Session = Depends(database.get_db)):
    texts = crud.get_texts(db)
    return {"contents": [{"id": text.id, "content": text.content} for text in texts]}
