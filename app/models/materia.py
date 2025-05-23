from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Materia(db.Model):
    __tablename__ = "materias"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    codigo = db.Column(db.String(20), nullable=False, unique=True)
    observacion = db.Column(db.String(255), nullable=True)