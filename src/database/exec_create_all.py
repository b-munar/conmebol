from src.database.base import Base
from src.database.engine import engine

from src.models.conmebol_model import GameModel, DateModel

table_objects = [GameModel.__table__, DateModel.__table__]

if __name__ == "__main__":
    Base.metadata.create_all(
        bind = engine(), 
        tables=table_objects,
        checkfirst=True
    )