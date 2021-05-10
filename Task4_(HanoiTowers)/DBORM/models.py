from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from DBORM import BaseModel


_Base = declarative_base()


class Iteration(_Base, BaseModel):
    __databasepath__ = '/Iterations.sqlite'

    percent = Column(Integer, primary_key=True)
    number = Column(Float)
    scheme = Column(String)
    disk_in_motion = Column(Integer, nullable=True)
    from_index = Column(Integer, nullable=True)
    to_index = Column(Integer, nullable=True)
    from_name = Column(Integer, nullable=True)
    to_name = Column(Integer, nullable=True)
