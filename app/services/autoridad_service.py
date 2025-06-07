from app.models import Autoridad
from app.repositories import AutoridadRepository

class AutoridadService:

    @staticmethod
    def crear(autoridad: Autoridad, materias: list = None):
        if materias:
            for materia in materias:
                autoridad.asociar_materia(materia)
        AutoridadRepository.crear(autoridad)

    @staticmethod
    def buscar_por_id(id: int) -> Autoridad:
        return AutoridadRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Autoridad]:
        return AutoridadRepository.buscar_todos()
    
    @staticmethod
    def actualizar(id: int, autoridad: Autoridad, materias:list = None) -> Autoridad:
        autoridad_existente = AutoridadRepository.buscar_por_id(id)
        if not autoridad_existente:
            return None
        autoridad_existente.nombre = autoridad.nombre
        autoridad_existente.telefono = autoridad.telefono
        autoridad_existente.email = autoridad.email
        autoridad_existente.cargo = autoridad.cargo
        
        if materias is not None:
            autoridad_existente.materias.clear()
            for materia in materias:
                autoridad_existente.asociar_materia(materia)
        
        AutoridadRepository.actualizar(autoridad_existente)
        return autoridad_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> bool:
        return AutoridadRepository.borrar_por_id(id)

    