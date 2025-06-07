from app.models import TipoDedicacion
from app.repositories import TipoDedicacionRepository

class TipoDedicacionService:

    @staticmethod
    def crear(tipodedicacion):
        """
        Crea un nuevo tipo dedicacion en la base de datos.
        :param tipodedicacion: Objeto TipoDedicacion a crear.
        :return: Objeto TipoDedicacion creado.
        """
        return TipoDedicacionRepository.crear(tipodedicacion)
    @staticmethod
    def buscar_por_id(id: int) -> TipoDedicacion:
        """
        Busca un tipo dedicacion por su ID.
        :param id: ID del tipo dedicacion a buscar.
        :return: Objeto TipoDedicacion encontrado o None si no se encuentra.
        """
        return TipoDedicacionRepository.buscar_por_id(id)
    @staticmethod
    def buscar_todos() -> list[TipoDedicacion]:
        """
        Busca todos los tipos de dedicacion en la base de datos.
        :return: Lista de objetos TipoDedicacion.
        """
        return TipoDedicacionRepository.buscar_todos()
    @staticmethod
    def actualizar(id: int, tipodedicacion: TipoDedicacion) -> TipoDedicacion:
        """
        Actualiza un tipo dedicacion en la base de datos.
        :param id: ID del tipo dedicacion a actualizar.
        :param tipodedicacion: Objeto TipoDedicacion actualizado.
        :return: Objeto TipoDedicacion actualizado.
        """
        tipodedicacion_existente = TipoDedicacionRepository.buscar_por_id(id)
        if not tipodedicacion_existente:
            return None
        tipodedicacion_existente.nombre = tipodedicacion.nombre
        tipodedicacion_existente.observacion = tipodedicacion.observacion
        return tipodedicacion_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> bool:
        return TipoDedicacionRepository.borrar_por_id(id)
    