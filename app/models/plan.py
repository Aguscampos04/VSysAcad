from dataclasses import dataclass
from app import db
from datetime import date

@dataclass(init=False, repr=True, eq=True)
class Plan(db.Model):
    __tablename__ = "planes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha_inicio = db.Column(db.Date, nullable=False)
    fecha_fin = db.Column(db.Date, nullable=False)
    observacion = db.Column(db.String(255), nullable=True)
    

