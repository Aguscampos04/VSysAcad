from app import db 
from app.models.materia import Materia

class MateriaRepository:

    @staticmethod
    def crear(materia):
        """
        Crea un nuevo objeto Materia en la base de datos.
        :param materia: Objeto Materia a crear.
        :return: Objeto Materia creado.
        """
        db.session.add(materia)
        db.session.commit()

    @staticmethod
    def buscar_por_id(id: int):
        """
        Busca un objeto Materia por su ID.
        :param id: ID del objeto Materia a buscar.
        :return: Objeto Materia encontrado o None si no se encuentra.
        """
        return db.session.query(Materia).filter_by(id = id).first()
    
    @staticmethod
    def buscar_todos():
        """
        Busca todos los objetos Materia en la base de datos.
        :return: Lista de objetos Materia encontrados.
        """
        return db.session.query(Materia).all()
    

    @staticmethod
    def actualizar(materia: Materia) -> Materia:
        """
        Actualiza un objeto Materia en la base de datos.
        :param materia: Objeto Materia a actualizar.
        :return: Objeto Materia actualizado.
        """
        materia_existente = db.session.merge(materia)
        if not materia_existente:
            return None
        return materia_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> bool:
        materia = db.session.query(Materia).filter_by(id=id).first()
        if not materia:
            return False
        db.session.delete(materia)
        db.session.commit()
        return True
    

    