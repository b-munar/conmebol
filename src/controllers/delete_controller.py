from src.models.conmebol_model import DateModel, GameModel
from src.database.session import Session
from flask_restful import Resource

class Delete(Resource):

    def delete(self, **kwargs):

        session = Session()

        query_dates =  session.query(DateModel)

        query_games = session.query(GameModel)

        query_games.delete()

        query_dates.delete()

        session.commit()

        return "Delete", 200