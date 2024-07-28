from sqlalchemy import Column, String, Integer
from src.database.base import Base

import enum
from sqlalchemy import Integer,  ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy_utils.types.choice import ChoiceType

class Team(enum.Enum):
    ARGENTINA = 1
    BOLIVIA = 2
    BRASIL = 3
    CHILE = 4
    COLOMBIA = 5
    ECUADOR = 6
    PARAGUAY = 7
    PERU = 8
    URUGUAY = 9
    VENEZUELA = 10

class DateModel(Base):
    __tablename__ = 'date'
    id = Column(Integer(), primary_key=True, autoincrement=False)
    game = relationship('GameModel')

class GameModel(Base):
    __tablename__ = 'game'
    id = Column(Integer(), primary_key=True)
    id_match =  Column(Integer(), nullable=False)
    id_local = Column(ChoiceType(Team, impl=Integer()))
    id_visitor = Column(ChoiceType(Team, impl=Integer()))
    gol_local =  Column(Integer(), nullable=False)
    gol_visitor =  Column(Integer(), nullable=False)
    date_id = Column(Integer(), ForeignKey('date.id'))
    date = relationship("DateModel")