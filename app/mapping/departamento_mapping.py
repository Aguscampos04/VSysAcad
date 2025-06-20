from marshmallow import fields, Schema, post_load, validate
from app.models import Departamento


class DepartamentoMapping(Schema):
    id = fields.Integer()
    nombre = fields.String(
        required=True, validate=validate.Length(min=1, max=50))

    @post_load
    def nuevo_departamento(self, data, **kwargs):
        return Departamento(**data)
