from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text
)

from .meta import Base


class Shop(Base):
    __tablename__ = 'shops'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    desc = Column(Text)
    adr = Column(Text)


Index('my_index', Shop.name, unique=True, mysql_length=255)
