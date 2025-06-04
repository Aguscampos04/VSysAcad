from dataclasses import dataclass
from app import db


@dataclass(init=False, repr=True, eq=True)
class Plan(db.Model):
    __tablename__ = "planes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50),nullable =False)
    fecha_inicio = db.Column(db.Date, nullable=False)
    fecha_fin = db.Column(db.Date, nullable=False)
    observacion = db.Column(db.String(255), nullable=True)
    

