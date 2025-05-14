import unittest
import os
from flask import current_app
from app import create_app
from app.models.facultad import Facultad

class FacultadTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_facultad_creation(self):
        facultad = Facultad()
        facultad.nombre = "Facultad de Ciencias"
        facultad.abreviatura = "FCC"
        facultad.directorio = "/facultad/ciencias"
        facultad.sigla = "FC"
        facultad.CodigoPostal = "12345"
        facultad.ciudad = "Ciudad"
        facultad.domicilio = "Calle 123"
        facultad.telefono = "123456789"
        facultad.contacto = "Juan Perez"
        facultad.email = "1234@gmail.com"
        self.assertIsNotNone(facultad)
        self.assertIsNotNone(facultad.nombre)
        self.assertEqual(facultad.nombre, "Facultad de Ciencias")
        self.assertEqual(facultad.abreviatura, "FCC")
        self.assertEqual(facultad.directorio, "/facultad/ciencias")