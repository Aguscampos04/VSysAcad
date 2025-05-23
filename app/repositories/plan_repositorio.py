from app import db
from app.models import Plan

class PlanRepository:
    @staticmethod
    def crear(plan):
        """
        Crea un nuevo plan en la base de datos.
        :param plan: Instancia de Plan a crear.
        :return: Instancia de Plan creada.
        """
        db.session.add(plan)
        db.session.commit()
      

    def buscar_por_id(id: int):
        """
        Busca un plan por su ID.
        :param id: ID del plan a buscar.
        :return: Instancia de Plan encontrada o None si no se encuentra.
        """
        return db.session.query(Plan).filter_by(id=id).first()
    
    def buscar_todos():
        """
        Busca todos los planes en la base de datos.
        :return: Lista de instancias de Plan.
        """
        return db.session.query(Plan).all()
    
    def actualizar(plan: Plan) -> Plan:
        """
        Actualiza un plan existente en la base de datos.
        :param plan: Instancia de Plan a actualizar.
        :return: Instancia de Plan actualizada.
        """
        plan_existente = db.session.merge(plan)
        if not plan_existente:
            return None
        return plan_existente
    
    def borrar_por_id(id: int) -> Plan:
        """
        Borra un plan por su ID.
        :param id: ID del plan a borrar.
        :return: Instancia de Plan borrada o None si no se encuentra.
        """
        plan = db.session.query(Plan).filter_by(id=id).first()
        if not plan:
            return None
        db.session.delete(plan)
        db.session.commit()
        return plan