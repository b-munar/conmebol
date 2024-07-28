from src.controllers.delete_controller import Delete
from src.controllers.table_controller import GameTable
from flask import Flask
from flask_restful import Api
from src.controllers.ping_controller import Ping
from src.controllers.conmebol_controller import DateGameController,DateGameCalendarController

def create_app():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Ping, '/conmebol/ping')
    api.add_resource(DateGameController, '/conmebol')
    api.add_resource(DateGameCalendarController, '/conmebol/calendar')
    api.add_resource(GameTable, '/conmebol/table')
    api.add_resource(Delete, '/conmebol/delete')
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=80, host='0.0.0.0')
else:
    gunicorn_app = create_app()