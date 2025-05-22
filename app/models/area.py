from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Area(db.Model):
    __tablename__ = 'areas'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50), nullable=False, unique=True)
    
