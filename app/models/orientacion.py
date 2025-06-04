from dataclasses import dataclass
from app.models import Especialidad, Plan, Materia
from app import db

@dataclass(init=False, repr=True, eq=True)
class Orientacion(db.Model):
    __tablename__ = "orientaciones"
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    nombre = db.Column(db.String(50), nullable = False)
    
    especialidad_id = db.Column(db.Integer, db.ForeignKey('especialidades.id'), nullable=False)
    especialidad = db.relationship('Especialidad', backref='orientaciones', lazy=True)
    
    plan_id = db.Column(db.Integer, db.ForeignKey('planes.id'), nullable=False)
    plan = db.relationship('Plan', backref='orientaciones', lazy=True)
    
    materia_id = db.Column(db.Integer, db.ForeignKey('materias.id'), nullable=False)
    materia = db.relationship('Materia', backref='orientaciones', lazy=True)

    