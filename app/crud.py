from sqlalchemy.orm import Session
from .models import Text

def get_texts(db: Session):
    return db.query(Text).all()
