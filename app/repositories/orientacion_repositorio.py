from app import db
from app.models import Orientacion
 
class OrientacionRepository:
    @staticmethod
    def crear(orientacion):
        db.session.add(orientacion)
        db.session.commit()

    @staticmethod
    def buscar_por_id(id: int):
        return db.session.query(Orientacion).filter_by(id=id).first()