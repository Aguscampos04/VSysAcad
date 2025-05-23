from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class TipoDocumento(db.Model):
    __tablename__ = 'tipodocumentos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dni = db.Column(db.Integer, nullable=False)
    libreta_civica = db.Column(db.String(20), nullable=False)
    libreta_enrolamiento = db.Column(db.String(20), nullable=False)
    pasaporte = db.Column(db.String(20), nullable=False)