from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Item(Base):
    __tablename__ = 'itens'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255))
    pt_br = Column(String(255))
    en_us = Column(String(255))