from sqlalchemy import Column, Integer, String, Date, Numeric
from app.database import Base
from pgvector.sqlalchemy import Vector

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Numeric(12, 2), nullable=False)
    category = Column(String, nullable=False)
    embedding = Column(Vector(384), nullable=True)