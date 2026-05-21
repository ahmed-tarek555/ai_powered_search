from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.schemas.product import ProductCreate
from app.db_models.product import Product
from app.database import get_db
from app.config import BASE_DIR
from app.models.embedder import get_embedding

templates = Jinja2Templates(directory=BASE_DIR / "templates")
router = APIRouter(prefix="/products")

@router.post("/add_product")
def add_product(product: ProductCreate, db: Session = Depends(get_db)):

    embedding = get_embedding(ProductCreate.description)
    new_product = Product(
        name=product.name,
        description=product.description,
        price=product.price,
        category=product.category,
        embedding=embedding,
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return {
        "id": new_product.id,
    }

@router.get("/")
async def get_page(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})