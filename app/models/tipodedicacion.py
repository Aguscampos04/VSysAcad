from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class TipoDedicacion(db.Model):
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ############# Atributos de la clase #############
    nombre: str = db.Column(db.String(100), nullable=False)
    observacion: str = db.Column(db.String(200), nullable=True)
