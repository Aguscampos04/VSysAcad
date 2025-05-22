from dataclasses import dataclass
from app import db
from app.models import TipoEspecialidad

@dataclass(init=False, repr=True, eq=True)
class Especialidad(db.Model):
    __tablename__ = 'especialidades'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    letra = db.Column(db.String(1), nullable=False)
    observacion = db.Column(db.String(255), nullable=True)
    tipoespecialidad_id = db.Column(db.Integer, db.ForeignKey('tipoespecialidades.id'), nullable=False)
    tipoespecialidad = db.relationship('TipoEspecialidad', backref='especialidades', lazy=True)