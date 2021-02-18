from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text
)

from .meta import Base


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    phone = Column(Text)
    sum = Column(Integer)
    shop_id = Column(Integer)
    products = Column(Text)


Index('my_index', Order.name, unique=True, mysql_length=255)
