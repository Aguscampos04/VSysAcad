from app.models import Orientacion
from app.repositories import OrientacionRepository

class OrientacionService:
    @staticmethod
    def crear(orientacion):
        OrientacionRepository.crear(orientacion)

    @staticmethod
    def buscar_por_id(id: int) -> Orientacion:        
        return OrientacionRepository.buscar_por_id(id)