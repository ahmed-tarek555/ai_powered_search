from fastapi import APIRouter, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import get_db
from app.config import BASE_DIR
from app.db_models.product import Product
from app.utils.utils import search

templates = Jinja2Templates(directory=BASE_DIR / "templates")
router = APIRouter(prefix="/search")

@router.post("/")
def seach(query: str, db: Session = Depends(get_db)):

    documents = db.query(Product).all()
    result = search(query, documents)

    return result