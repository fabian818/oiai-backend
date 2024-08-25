from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from . import models, crud, database

app = FastAPI()

origins = [
    "http://localhost:5173",  # Origen específico permitido
    "http://localhost",       # Otro origen que podrías querer permitir
    # Agrega más orígenes si es necesario
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

@app.get('/text')
def read_text(db: Session = Depends(database.get_db)):
    texts = crud.get_texts(db)
    return {"contents": [{"id": text.id, "content": text.content} for text in texts]}
