from app.models import Facultad
from app.repositories.facultad_repositorio import FacultadRepository
class FacultadSerice:

    @staticmethod
    def crear_facultad(facultad:Facultad):
       FacultadRepository.crear(Facultad)