from marshmallow import Schema, fields
from src.models.conmebol_model import Team
import re
from functools import partial

_snake_case = re.compile(r"(?<=\w)_(\w)")
_to_camel_case = partial(_snake_case.sub, lambda m: m[1].upper())

class CamelCasedSchema(Schema):
    """Gives fields a camelCased data key"""
    def on_bind_field(self, field_name, field_obj, _cc=_to_camel_case):
        field_obj.data_key = _cc(field_name.lower())


class Date(Schema):
    id = fields.Integer()

class Game(CamelCasedSchema):
    id_match = fields.Integer()
    id_local = fields.Integer()
    id_visitor = fields.Integer()
    gol_local = fields.Integer()
    gol_visitor = fields.Integer()

class DateGame(Schema):
    date = fields.Nested(Date)
    games = fields.List(fields.Nested(Game))

class ConmebolSerializeSchema(Schema):
    name = fields.String()

class GameSerialize(Schema):
    id_match = fields.Integer(data_key="idMatch")
    id_local = fields.Enum(Team, by_value=True, data_key="idLocal")
    id_visitor = fields.Enum(Team, by_value=True, data_key="idVisitor")
    gol_local = fields.Integer(data_key="golLocal")
    gol_visitor = fields.Integer(data_key="golVisitor")