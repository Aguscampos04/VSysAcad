import unittest
import os
from flask import current_app
from app import create_app
from app.models import Orientacion, Especialidad, Plan, Materia ,TipoEspecialidad
from app.services import TipoEspecialidadService, EspecialidadService, PlanService, MateriaService
from app.services import OrientacionService
from app import db
from datetime import date



class OrientacionTestCase(unittest.TestCase):
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

    def test_orientacion_creation(self):
        orientacion = self.__nuevaorientacion()
        self.assertIsNotNone(orientacion)
        self.assertIsNotNone(orientacion.nombre)
        self.assertEqual(orientacion.nombre, "Orientacion A")
        self.assertEqual(orientacion.especialidad.tipoespecialidad.nombre, "Tipo 1")


    def test_crear(self):
        orientacion = self.__nuevaorientacion()
        self.assertIsNotNone(orientacion)
        self.assertIsNotNone(orientacion.nombre)
        self.assertGreaterEqual(orientacion.nombre, "Orientacion A")
        self.assertEqual(orientacion.especialidad.tipoespecialidad.nombre, "Tipo 1")
        self.assertEqual(orientacion.plan.fecha_inicio, date(2025,1,2))
        self.assertIsNotNone(orientacion.materia.nombre, "Desarrollo")

    def test_busqueda(self):
        orientacion = self.__nuevaorientacion()
        OrientacionService.crear(orientacion)
        r=OrientacionService.buscar_por_id(orientacion.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Orientacion A")


    def __nuevaorientacion(self, codigo= "SQL"):
        tipo_especialidad = TipoEspecialidad()
        tipo_especialidad.nombre = "Tipo 1"
        TipoEspecialidadService.crear(tipo_especialidad)

        especialidad = Especialidad()
        especialidad.nombre = "matematica"
        especialidad.letra = "l"
        especialidad.tipoespecialidad = tipo_especialidad
        EspecialidadService.crear(especialidad)

        plan = Plan()
        plan.fecha_inicio = date(2025,1,2)
        plan.fecha_fin = date(2025,2,3)
        PlanService.crear(plan)


        materia = Materia()
        materia.nombre = "Desarrollo"
        materia.codigo = codigo
        MateriaService.crear(materia)

        orientacion = Orientacion()
        orientacion.nombre = "Orientacion A"
        orientacion.especialidad = especialidad
        orientacion.plan = plan
        orientacion.materia = materia
        return orientacion





