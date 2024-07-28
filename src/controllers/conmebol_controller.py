from flask_restful import Resource
from flask import request

from src.database.session import Session
from src.models.conmebol_model import DateModel, GameModel
from src.schemas.conmebol_schema import DateGame, GameSerialize

from src.models.conmebol_model import Team
from src.utils.generate_round_robin_schedule import generate_double_round_robin_schedule


class DateGameController(Resource):
    def post(self, **kwargs):
        if(request.data):
            request_json = request.get_json()
        else:
            return "", 400
        
        date_game_create_schema = DateGame()
        
        errors = date_game_create_schema.validate(request_json)
        if errors:
            return "incorrect structure", 400
        
        conmebol_create_dump = date_game_create_schema.load(request_json)

        if not len(conmebol_create_dump['games']) == 5:
            return "there are 5 games to date", 400
        
        if conmebol_create_dump['date']['id'] < 1 or conmebol_create_dump['date']['id'] > 18:
            return "the id is out of the date range", 400

        session = Session()

        query_date = session.query(DateModel).filter(DateModel.id==conmebol_create_dump['date']['id']).count()

        if query_date>0:
            session.close()
            return "date already exists", 400
        
        new_date = DateModel(**conmebol_create_dump['date'])
        session.add(new_date)

        for game in conmebol_create_dump['games']:
            game["date_id"] = conmebol_create_dump['date']['id']
            new_game = GameModel(**game)
            session.add(new_game)

        session.commit()

        return "created", 201

    def get(self, **kwargs):

        dates = []

        session = Session()

        query_dates =  session.query(DateModel)

        list_query_dates = [date.id for date in query_dates]

        list_query_position = [date.id - 1 for date in query_dates]

        for query_date in query_dates:

            date_games = {"date":{}, "games":[]}

            date_games["date"]["id"] = query_date.id

            date_games["date"]["position"] = query_date.id -1

            query_games = session.query(GameModel).filter(GameModel.date_id==query_date.id)

            game_schema = GameSerialize()

            for query_game in query_games:
                date_games["games"].append(game_schema.dump(query_game))
            
            dates.append(date_games)


        session.close()


        return {"listDate": list_query_dates, "listPosition": list_query_position, "dateGames": dates}, 200
    

class DateGameCalendarController(Resource):
    def get(self, **kwargs):

        teams = [e.value for e in Team]

        schedule = generate_double_round_robin_schedule(teams)

        return {"listDates": schedule }, 200
