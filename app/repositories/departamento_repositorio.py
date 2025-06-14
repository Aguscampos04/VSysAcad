from app import db
from app.models import Departamento

class DepartamentoRepository:

    @staticmethod
    def crear(departamento):
        db.session.add(departamento)
        db.session.commit()

    @staticmethod
    def buscar_por_id(id: int):
        return db.session.query(Departamento).filter_by(id=id).first()
    
    @staticmethod
    def buscar_todos():
        return db.session.query(Departamento).all()
    
    @staticmethod
    def actualizar(departamento) -> Departamento:
        departamento_existente = db.session.merge(departamento)
        if not departamento_existente:
            return None
        return departamento_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> bool:
        departamento = db.session.query(Departamento).filter_by(id=id).first()
        if not departamento:
            return False
        db.session.delete(departamento)
        db.session.commit()
        return True