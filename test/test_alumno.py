import unittest
import os
from flask import current_app
from app import create_app
from datetime import date
from app.models.tipodocumento import TipoDocumento
from app.models.alumno import Alumno

class AlumnoTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_alumno_creation(self):
        alumno = Alumno()
        alumno.nombre = "Juan"
        alumno.apellido = "Pérez"
        alumno.nrodocumento = "12345678"
        tipo_documento = TipoDocumento()
        tipo_documento.pasaporte = "nacional"
        alumno.tipo_documento = tipo_documento
        alumno.fecha_nacimiento = "2000-01-01"
        alumno.sexo = "M"
        alumno.nro_legajo = 123456
        alumno.fecha_ingreso = date(2020,1,1)
        self.assertIsNotNone(alumno)
        self.assertIsNotNone(alumno.nombre)
        self.assertEqual(alumno.nombre, "Juan")
        self.assertEqual(alumno.apellido, "Pérez")
        self.assertEqual(alumno.tipo_documento.pasaporte, "nacional")
        