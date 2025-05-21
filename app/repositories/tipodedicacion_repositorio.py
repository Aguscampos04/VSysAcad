from app import db
from app.models import TipoDedicacion

class TipoDedicacionRepository:
    @staticmethod
    def crear(tipodedicacion):
        """
        Crea un nuevo tipo dedicacion en la base de datos.
        :param tipodedicacion: Objeto TipoDedicacion a crear.
        :return: Objeto TipoDedicacion creado.
        """
        db.session.add(tipodedicacion)
        db.session.commit()
    
    @staticmethod
    def buscar_por_id(id: int):
        """
        Busca un tipo dedicacion por su ID.
        :param id: ID del tipo dedicacion a buscar.
        :return: Objeto TipoDedicacion encontrado o None si no se encuentra.
        """
        return db.session.query(TipoDedicacion).filter_by(id=id).first()
    @staticmethod
    def buscar_todos():
        """
        Busca todos los tipos de dedicacion en la base de datos.
        :return: Lista de objetos TipoDedicacion.
        """
        return db.session.query(TipoDedicacion).all()
    @staticmethod
    def actualizar(tipodedicacion) -> TipoDedicacion:
        """
        Actualiza un tipo dedicacion en la base de datos.
        :param tipodedicacion: Objeto TipoDedicacion a actualizar.
        :return: Objeto TipoDedicacion actualizado.
        """
        tipodedicacion_existente = db.session.merge(TipoDedicacion)
        if not tipodedicacion_existente:
            return None
        return tipodedicacion_existente
    @staticmethod
    def borrar_por_id(id: int) ->TipoDedicacion:
        """
        Borra un tipo dedicacion por su ID.
        :param id: ID del tipo dedicacion a borrar.
        """
        tipodedicacion = db.session.query(TipoDedicacion).filter_by(id=id).first()
        if not tipodedicacion:
            return None
        db.session.delete(tipodedicacion)
        db.session.commit()
        return tipodedicacion