from app.models import Area
from app.repositories import AreaRepository

class AreaService:
    @staticmethod
    def crear(area):
        """
        Crea un nuevo área en la base de datos.
        :param area: El área a crear.
        :return: El área creada.
        """
        AreaRepository.crear(area)
    
    @staticmethod
    def buscar_por_id(id: int) -> Area:
        """
        Busca un área por su ID.
        :param area_id: El ID del área a buscar.
        :return: El área encontrada o None si no existe.
        """
        return AreaRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Area]:
        """
        Busca todas las áreas en la base de datos.
        :return: Una lista de todas las áreas.
        """
        return AreaRepository.buscar_todos()
    
    @staticmethod
    def actualizar(id: int, area: Area) -> Area:
        """
        Actualiza un área existente en la base de datos.
        :param area_id: El ID del área a actualizar.
        :param area: El nuevo objeto área con los datos actualizados.
        :return: El área actualizada.
        """
        area_existente = AreaRepository.buscar_por_id(id)
        if not area_existente:
            return None
        area_existente.nombre = area.nombre
        return area_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Area:
        area = AreaRepository.borrar_por_id(id)
        if not area:
            return None
        return area
    
