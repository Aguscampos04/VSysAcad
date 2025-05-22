import unittest
import os
from flask import current_app
from app import create_app
from app.models.area import Area
from app.services import AreaService
from app import db

class AreaTestCase(unittest.TestCase):
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

    def test_area_creation(self):
        area = self.__nuevaarea()
        self.assertIsNotNone(area)
        self.assertIsNotNone(area.nombre)
        self.assertEqual(area.nombre, "matematica")
    
    def test_crear(self):
        area = self.__nuevaarea()
        AreaService.crear(area)
        self.assertIsNotNone(area)
        self.assertIsNotNone(area.id)
        self.assertGreaterEqual(area.id, 1)
        self.assertEqual(area.nombre, "matematica")

    def test_busqueda(self):
        area = self.__nuevaarea()
        AreaService.crear(area)
        r = AreaService.buscar_por_id(area.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "matematica")

    def test_buscar_todos(self):
        area1 = self.__nuevaarea("matematica")
        area2 = self.__nuevaarea("nombre2")
        AreaService.crear(area1)
        AreaService.crear(area2)
        areas = AreaService.buscar_todos()
        self.assertIsNotNone(areas)
        self.assertEqual(len(areas), 2)

    def test_actualizar(self):
        area = self.__nuevaarea()
        AreaService.crear(area)
        area.nombre = "nombre actualizado"
        area_actualizado = AreaService.actualizar(area.id, area)
        self.assertEqual(area_actualizado.nombre, "nombre actualizado")

    def test_borrar(self):
        area = self.__nuevaarea()
        AreaService.crear(area)
        AreaService.borrar_por_id(area.id)
        resultado = AreaService.buscar_por_id(area.id)
        self.assertIsNone(resultado)

    def __nuevaarea(self, nombre="matematica"):
        area = Area()
        area.nombre = nombre
        return area