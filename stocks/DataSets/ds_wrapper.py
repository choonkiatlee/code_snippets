from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timedelta
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
import sqlalchemy as sqlalchemy

# First Create a declarative base
Base = declarative_base()

class tick(Base):
    __tablename__ = 'test'
    date = Column(sqlalchemy.Date,primary_key=True)
    open=Column(sqlalchemy.Float)
    high = Column(sqlalchemy.Float)
    low = Column(sqlalchemy.Float)
    adj_close = Column(sqlalchemy.Float)
    volume = Column(sqlalchemy.BigInteger)