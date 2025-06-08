from app.models import Facultad
from app.repositories import FacultadRepository

class FacultadService:
    
    @staticmethod
    def crear(facultad: Facultad):
        FacultadRepository.crear(facultad)
    
    @staticmethod
    def buscar_por_id(id: int) -> Facultad:
        return FacultadRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Facultad]:
        return FacultadRepository.buscar_todos()
    
    @staticmethod
    def actualizar(id: int, facultad: Facultad) -> Facultad:
        facultad_existente = FacultadRepository.buscar_por_id(id)
        if not facultad_existente:
            return None
        facultad_existente.nombre = facultad.nombre
        facultad_existente.abreviatura = facultad.abreviatura
        facultad_existente.directorio = facultad.directorio
        facultad_existente.sigla = facultad.sigla
        facultad_existente.codigopostal = facultad.codigopostal
        facultad_existente.ciudad = facultad.ciudad
        facultad_existente.domicilio = facultad.domicilio
        facultad_existente.telefono = facultad.telefono
        facultad_existente.contacto = facultad.contacto
        facultad_existente.email = facultad.email
        facultad_existente.universidad = facultad.universidad
        return facultad_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> bool:
        return FacultadRepository.borrar_por_id(id)