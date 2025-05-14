
from app import db


class FacultadRepository:
    @staticmethod
    def crear(facultad):
        
        db.session.add(facultad)
        db.session.commit()