from app.models import Materia
from app.repositories import MateriaRepository


class MateriaService:
    """
    Clase de servicio para gestionar las operaciones relacionadas con la entidad Materia.
    """

    @staticmethod
    def crear(materia: Materia) -> Materia:
        """
        Crea un nuevo objeto Materia en la base de datos.
        :param materia: Objeto Materia a crear.
        :return: Objeto Materia creado.
        """
        MateriaRepository.crear(materia)

    @staticmethod
    def buscar_por_id(id: int) -> Materia:
        """
        Busca un objeto Materia por su ID.
        :param id: ID del objeto Materia a buscar.
        :return: Objeto Materia encontrado o None si no se encuentra.
        """
        return MateriaRepository.buscar_por_id(id)

    @staticmethod
    def buscar_todos() -> list[Materia]:
        """
        Busca todos los objetos Materia en la base de datos.
        :return: Lista de objetos Materia encontrados.
        """
        return MateriaRepository.buscar_todos()

    @staticmethod
    def actualizar(id: int, materia: Materia) -> Materia:
        """
        Actualiza un objeto Materia en la base de datos.
        :param materia: Objeto Materia a actualizar.
        :return: Objeto Materia actualizado.
        """
        materia_existente = MateriaRepository.buscar_por_id(materia.id)
        if not materia_existente:
            return None
        materia_existente.nombre = materia.nombre
        materia_existente.codigo = materia.codigo
        materia_existente.observacion = materia.observacion
        return materia_existente

    @staticmethod
    def borrar_por_id(id: int) -> Materia:
        """
        Borra un objeto Materia por su ID.
        :param id: ID del objeto Materia a borrar.
        :return: True si se borra correctamente, False en caso contrario.
        """
        return MateriaRepository.borrar_por_id(id)
