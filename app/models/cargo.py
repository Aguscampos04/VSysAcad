from dataclasses import dataclass
from app.models import CategoriaCargo, TipoDedicacion
from app import db

@dataclass(init=False, repr=True, eq=True)
class Cargo(db.Model):
    __tablename__ = 'cargos'
    id = db.Column(db.Integer, primary_key=True,auto_increment=True)
    nombre = db.Column(db.String(50), nullable=False)
    puntos = db.Column(db.Integer, nullable = True)
    categoria_cargo_id = db.Column(db.Integer, db.ForeignKey('categoriacargos.id'), nullable=False)
    categoria_cargo = db.relationship('CategoriaCargo', backref='cargos', lazy=True)
    tipo_dedicacion_id = db.Column(db.Integer, db.ForeignKey('tipodedicaciones.id'), nullable=False)
    tipo_dedicacion = db.relationship('TipoDedicacion', backref='cargos', lazy=True)