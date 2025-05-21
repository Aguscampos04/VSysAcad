from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Plan(db.Model):
    __tablename__ = "planes"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #TODO: CAMBIAR A DATETIME
    fecha_inicio = db.Column(db.String(10), nullable=False)
    fecha_fin = db.Column(db.String(10), nullable=False)
    observacion = db.Column(db.String(255), nullable=True)
    

