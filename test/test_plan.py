import unittest
import os
from flask import current_app
from app import create_app
from app.models.plan import Plan
from app.services import PlanService
from app import db

class PlanTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_plan_creation(self):
        plan = self.__nuevoplan()
        self.assertEqual(plan.nombre, "Plan A")
        self.assertEqual(plan.fecha_inicio, "2023-01-01")
        self.assertEqual(plan.fecha_fin, "2023-12-31")

    def test_crear(self):
        plan = self.__nuevoplan()
        PlanService.crear(plan)
        self.assertIsNotNone(plan)
        self.assertIsNotNone(plan.id)
        self.assertGreaterEqual(plan.id, 1)
        self.assertEqual(plan.nombre, "Plan A")
    
    def test_busqueda(self):
        plan = self.__nuevoplan()
        PlanService.crear(plan)
        r= PlanService.buscar_por_id(plan.id)   
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, plan.nombre)
        self.assertEqual(r.fecha_inicio, plan.fecha_inicio)
        self.assertEqual(r.fecha_fin, plan.fecha_fin)
        self.assertEqual(r.observacion, plan.observacion)


    def test_buscar_todos(self):
        plan1 = self.__nuevoplan()
        plan2 = self.__nuevoplan("Plan B","2023-06-01","2023-12-31", "Observacion de prueba 2")
        PlanService.crear(plan1)
        PlanService.crear(plan2)
        planes = PlanService.buscar_todos()
        self.assertIsNotNone(planes)
        self.assertEqual(len(planes), 2)
    
    def test_actualizar_plan(self):
        plan= self.__nuevoplan()
        PlanService.crear(plan)
        plan.nombre = "Plan Actualizado"
        plan.fecha_inicio = "2023-02-01"
        plan.fecha_fin = "2023-11-30"
        plan.observacion = "Observacion actualizada"

    def test_borrar_por_id(self):
        plan = self.__nuevoplan()
        PlanService.crear(plan)
        PlanService.borrar_por_id(plan.id)
        r= PlanService.buscar_por_id(plan.id)
        self.assertIsNone(r)

        
        

    

    def __nuevoplan(self, nombre= "Plan A", fecha_inicio= "2023-01-01", fecha_fin= "2023-12-31", observacion= "Observacion de prueba"):
        plan = Plan()
        plan.nombre = nombre
        plan.fecha_inicio = fecha_inicio
        plan.fecha_fin = fecha_fin
        plan.observacion = observacion
        return plan