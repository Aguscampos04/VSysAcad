from marshmallow import fields, Schema, post_load
from app.models.universidad import Universidad


class UniversidadMapping(Schema):
    id = fields.Integer(dump_only=True) 
    nombre = fields.String(required = True)
    sigla = fields.String(required = True)

    @post_load
    def nueva_universidad(self,data,**kwargs):
        return Universidad(**data)
