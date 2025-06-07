from app.models import Materia
from app.repositories import MateriaRepository


class MateriaService:

    #TODO preguntar a profe si esta bien relacion muchos a muchos en service,test modelos de autoridad y materia
    @staticmethod
    def crear(materia: Materia, autoridades: list = None) -> Materia:
        if autoridades:
            for autoridad in autoridades:
             materia.asociar_autoridad(autoridad)
        MateriaRepository.crear(materia)
        return materia

    @staticmethod
    def buscar_por_id(id: int) -> Materia:
        return MateriaRepository.buscar_por_id(id)

    @staticmethod
    def buscar_todos() -> list[Materia]:
        return MateriaRepository.buscar_todos()

    @staticmethod
    def actualizar(id: int, materia: Materia, autoridades: list = None) -> Materia:
        materia_existente = MateriaRepository.buscar_por_id(id)
        if not materia_existente:
            return None

        materia_existente.nombre = materia.nombre
        materia_existente.codigo = materia.codigo
        materia_existente.observacion = materia.observacion
        
        if autoridades is not None:
            materia_existente.autoridades.clear()
            for autoridad in autoridades:
                materia_existente.asociar_autoridad(autoridad)
        
        MateriaRepository.actualizar(materia_existente)
        return materia_existente

    @staticmethod
    def borrar_por_id(id: int) -> bool:
        return MateriaRepository.borrar_por_id(id)