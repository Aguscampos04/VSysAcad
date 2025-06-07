from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class TipoDocumento(db.Model):
    __tablename__ = 'tipodocumentos'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dni: int = db.Column(db.Integer, nullable=False)
    libreta_civica: str = db.Column(db.String(20), nullable=False)
    libreta_enrolamiento: str = db.Column(db.String(20), nullable=False)
    pasaporte: str = db.Column(db.String(20), nullable=False)