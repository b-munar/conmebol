    
import pandas as pd
from flask_restful import Resource
from src.models.conmebol_model import GameModel
from src.utils.actualizar_datos import actualizar_datos
from src.database.session import Session


class GameTable(Resource):
    def get(self, **kwards):

        data = {
            'id': [],
            'played': [],
            'won': [],
            'drawn': [],
            'lost': [],
            'gf': [],
            'ga': [],
            'gd': [],
            'points': []
        }

        df = pd.DataFrame(data)


        session = Session()

        query_games = session.query(GameModel)

        for game in query_games:
            df = actualizar_datos(df, game.id_local.value, game.gol_local, game.gol_visitor)
            df = actualizar_datos(df, game.id_visitor.value, game.gol_visitor, game.gol_local)
        session.close()

        print(df)

        return df.to_dict('records')


