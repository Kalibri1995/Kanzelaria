from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text
)

from .meta import Base


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    desc = Column(Text)
    price = Column(Integer)
    adr = Column(Text)


Index('my_index', Product.name, unique=True, mysql_length=255)
