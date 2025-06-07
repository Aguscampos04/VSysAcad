from app.models import Autoridad
from app.repositories import AutoridadRepository, MateriaRepository
from app import db

class AutoridadService:
    @staticmethod
    def crear(autoridad):
        AutoridadRepository.crear(autoridad)

    @staticmethod
    def buscar_por_id(id: int) -> Autoridad:
         return AutoridadRepository.buscar_por_id(id)

    @staticmethod
    def buscar_todos() -> list[Autoridad]:
       return AutoridadRepository.buscar_todos()

    @staticmethod
    def actualizar(id: int, autoridad: Autoridad) -> Autoridad:
        autoridad_existente = AutoridadRepository.buscar_por_id(id)
        if not autoridad_existente:
            return None
        autoridad_existente.nombre = autoridad.nombre
        autoridad_existente.telefono = autoridad.telefono
        autoridad_existente.email = autoridad.email
        return autoridad_existente

    @staticmethod
    def borrar_por_id(id: int) -> bool:
        return AutoridadRepository.borrar_por_id(id)

    @staticmethod
    def asociar_materia(autoridad_id: int, materia_id: int):
        autoridad = AutoridadRepository.buscar_por_id(autoridad_id)
        materia = MateriaRepository.buscar_por_id(materia_id)
        if not autoridad or not materia:
            raise ValueError("Materia o autoridad no encontrada")
        autoridad.asociar_materia(materia)
        

    @staticmethod
    def desasociar_materia(autoridad_id: int, materia_id: int):
        autoridad = AutoridadRepository.buscar_por_id(autoridad_id)
        materia = MateriaRepository.buscar_por_id(materia_id)
        if not autoridad or not materia:
            raise ValueError("Materia o autoridad no encontrada")
        autoridad.desasociar_materia(materia)
        
