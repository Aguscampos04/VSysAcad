from marshmallow import fields, Schema, post_load, validate
from app.models import Grupo

class GrupoMapping(Schema):
    id = fields.Integer()
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=20))
    
    @post_load
    def nueva_grupo(self, data, **kwargs):
        return Grupo(**data)