from app import db
from app.models import CategoriaCargo

class CategoriaCargoRepository:

    @staticmethod
    def crear(categoria):
        db.session.add(categoria)
        db.session.commit()

    @staticmethod
    def buscar_por_id(id: int):
        return db.session.query(CategoriaCargo).filter_by(id=id).first()
    
    @staticmethod
    def buscar_todos():
        return db.session.query(CategoriaCargo).all()
    
    @staticmethod
    def actualizar(categoria) -> CategoriaCargo:
        categoria_existente = db.session.merge(categoria)
        if not categoria_existente:
            return None
        return categoria_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> CategoriaCargo:
        categoria = db.session.query(CategoriaCargo).filter_by(id=id).first()
        if not categoria:
            return None
        db.session.delete(categoria)
        db.session.commit()
        return categoria