from fastapi import APIRouter, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import get_db
from app.config import BASE_DIR
from app.db_models.product import Product
from app.utils.utils import search
from app.schemas.search import SearchRequest

templates = Jinja2Templates(directory=BASE_DIR / "templates")
router = APIRouter(prefix="/search")

@router.post("/")
def seach(user_input: SearchRequest, db: Session = Depends(get_db)):

    products = db.query(Product).all()
    result = [
        {
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "category": product.category,
            "embedding": product.embedding
        }
        for product in products
    ]

    search_output = search(user_input.query, result)

    return search_output
