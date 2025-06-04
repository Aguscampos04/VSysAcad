import unittest
import os
from flask import current_app
from app import create_app
from app.models.cargo import Cargo
from app.models import CategoriaCargo,TipoDedicacion
from app.services import CargoService
from test.instancias import nuevacategoriacargo,nuevotipodedicacion
from app import db

class CargoTestCase(unittest.TestCase):
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
        cargo = self.__nuevocargo()
        CargoService.crear(cargo)
        self.assertIsNotNone(cargo)
        self.assertIsNotNone(cargo.nombre)
        self.assertGreaterEqual(cargo.nombre, "profesor")
        self.assertEqual(cargo.categoria_cargo.nombre, "Docente")
        self.assertEqual(cargo.tipo_dedicacion.nombre, "Dedicacion Completa")

    def test_busqueda(self):
        cargo = self.__nuevocargo()
        CargoService.crear(cargo)
        r=CargoService.buscar_por_id(cargo.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "profesor")
        self.assertEqual(r.tipo_dedicacion.nombre, "Dedicacion Completa")

    def test_buscar_todos(self):
        cargo1 = self.__nuevocargo()
        cargo2 = self.__nuevocargo()
        CargoService.crear(cargo1)
        CargoService.crear(cargo2)
        cargos = CargoService.buscar_todos()
        self.assertIsNotNone(cargos)
        self.assertEqual(len(cargos), 2)

    def test_actualizar(self):
        cargo = self.__nuevocargo()
        CargoService.crear(cargo)
        cargo.nombre = "profe actualizado"
        cargo_actualizado = CargoService.actualizar(cargo.id, cargo)
        self.assertEqual(cargo_actualizado.nombre, "profe actualizado")

    def test_borrar(self):
        cargo = self.__nuevocargo()
        CargoService.crear(cargo)
        CargoService.borrar_por_id(cargo.id)
        resultado = CargoService.buscar_por_id(cargo.id)
        self.assertIsNone(resultado)
    
    def __nuevocargo(self):
        cargo = Cargo()
        cargo.nombre = "profesor"
        cargo.puntos = 10
        cargo.categoria_cargo = nuevacategoriacargo()
        cargo.tipo_dedicacion = nuevotipodedicacion()
        return cargo