from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class CategoriaCargo(db.Model):
    __tablename__ = 'categoriacargos'
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    nombre = db.Column(db.String(30), nullable=False)