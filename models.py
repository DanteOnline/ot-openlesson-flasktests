from database import Base
# from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, \
    String, ForeignKey, Float


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), unique=True)
    description = Column(String, nullable=True)
    products = relationship('Product', back_populates='category')

    def __str__(self):
        return self.name


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), unique=True)
    description = Column(String, nullable=True)
    price = Column(Float, default=0)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category', back_populates='products')
