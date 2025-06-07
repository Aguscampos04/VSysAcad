from app.models import Plan
from app.repositories import PlanRepository

class PlanService:
    @staticmethod
    def crear(plan):
        """
        Crea un nuevo plan en la base de datos.
        :param plan: Instancia de Plan a crear.
        :return: Instancia de Plan creada.
        """
        PlanRepository.crear(plan)
    
    @staticmethod
    def buscar_por_id(id: int) -> Plan:
        """
        Busca un plan por su ID.
        :param id: ID del plan a buscar.
        :return: Instancia de Plan encontrada o None si no se encuentra.
        """
        return PlanRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Plan]:
        """
        Busca todos los planes en la base de datos.
        :return: Lista de instancias de Plan.
        """
        return PlanRepository.buscar_todos()
    
    @staticmethod
    def actualizar(id : int, plan: Plan) -> Plan:
        """
        Actualiza un plan existente en la base de datos.
        :param plan: Instancia de Plan a actualizar.
        :return: Instancia de Plan actualizada.
        """
        plan_existente = PlanRepository.buscar_por_id(plan.id)
        if not plan_existente:
            return None
        plan_existente.fecha_inicio = plan.fecha_inicio
        plan_existente.fecha_fin = plan.fecha_fin
        plan_existente.observacion = plan.observacion
        return plan_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> bool:
        return PlanRepository.borrar_por_id(id)