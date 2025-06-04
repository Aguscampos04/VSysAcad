import unittest
import os
from flask import current_app
from app import create_app
from app.models.autoridad import Autoridad
from app.models.cargo import Cargo
from test.instancias import nuevocargo

#TODO hay que hacer la relacion muchos a muchos con materia
class AutoridadTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_autoridad_creation(self):
        autoridad = self.__nuevaautoridad()
        self.assertIsNotNone(autoridad)
        self.assertIsNotNone(autoridad.nombre)
        self.assertEqual(autoridad.nombre, "Pelo")
        self.assertEqual(autoridad.cargo.nombre, "Profesor")
        self.assertEqual(autoridad.telefono, "123456789")

    def __nuevaautoridad(self):
        autoridad = Autoridad()
        autoridad.nombre = "Pelo"
        autoridad.cargo = nuevocargo()
        autoridad.telefono = "123456789"
        autoridad.email = "123@gmail.com"
        return autoridad