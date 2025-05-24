from app.models import Orientacion
from app.repositories import OrientacionRepository

class OrientacionService:
    @staticmethod
    def crear(orientacion):
        OrientacionRepository.crear(orientacion)

    @staticmethod
    def buscar_por_id(id: int) -> Orientacion:        
        return OrientacionRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Orientacion]:
        return OrientacionRepository.buscar_todos()
    
    @staticmethod
    def actualizar(id: int, orientacion: Orientacion) -> Orientacion:
        orientacion_existente = OrientacionRepository.buscar_por_id(id)
        if not orientacion_existente:
            return None
        orientacion_existente.nombre = orientacion.nombre
        orientacion_existente.especialidad_id = orientacion.especialidad_id
        orientacion_existente.plan_id = orientacion.plan_id
        orientacion_existente.materia_id = orientacion.materia_id
        return orientacion_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Orientacion:
        orientacion = OrientacionRepository.borrar_por_id(id)
        if not orientacion:
            return None
        return orientacion