import unittest
import os
from flask import current_app
from app import create_app
from app.models import Orientacion
from app.services import OrientacionService
from test.instancias import nuevaespecialidad, nuevoplan, nuevamateria
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


    def test_crear(self):
        orientacion = self.__nuevaorientacion()
        self.assertIsNotNone(orientacion)
        self.assertIsNotNone(orientacion.nombre)
        self.assertGreaterEqual(orientacion.nombre, "Orientacion A")
        self.assertEqual(orientacion.especialidad.tipoespecialidad.nombre, "Cardiologia")
        self.assertEqual(orientacion.plan.fecha_inicio, date(2024,6,4))
        self.assertIsNotNone(orientacion.materia.nombre, "Desarrollo")

    def test_busqueda(self):
        orientacion = self.__nuevaorientacion()
        OrientacionService.crear(orientacion)
        r=OrientacionService.buscar_por_id(orientacion.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Orientacion A")

    def test_buscar_todos(self):
        orientacion1 = self.__nuevaorientacion()
        
        orientacion2 = self.__nuevaorientacion(
        nombre="Orientacion B",
        codigo_materia="MAT102",
        nombre_especialidad="Neurología",
        nombre_plan="Plan 2025")

        OrientacionService.crear(orientacion1)
        OrientacionService.crear(orientacion2)
        orientaciones = OrientacionService.buscar_todos()
        self.assertIsNotNone(orientaciones)
        self.assertGreaterEqual(len(orientaciones), 2)

    def test_actualizar(self):
        orientacion = self.__nuevaorientacion()
        OrientacionService.crear(orientacion)
        orientacion.nombre = "Orientacion Actualizada"
        orientacion_actualizada = OrientacionService.actualizar(orientacion.id, orientacion)
        self.assertEqual(orientacion_actualizada.nombre, "Orientacion Actualizada")

    def test_borrar(self):
        orientacion = self.__nuevaorientacion()
        OrientacionService.crear(orientacion)
        OrientacionService.borrar_por_id(orientacion.id)
        resultado = OrientacionService.buscar_por_id(orientacion.id)
        self.assertIsNone(resultado)


    def __nuevaorientacion(self, nombre="Orientacion A", codigo_materia="MAT101", nombre_especialidad="Cardiologia",nombre_plan="Plan 2024"):
        orientacion = Orientacion()
        orientacion.nombre = nombre
        orientacion.especialidad = nuevaespecialidad(nombre=nombre_especialidad)
        orientacion.plan = nuevoplan(nombre=nombre_plan)
        orientacion.materia = nuevamateria(codigo=codigo_materia)
        return orientacion





