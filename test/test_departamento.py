import unittest
import os
from flask import current_app
from app import create_app
from app.models.departamento import Departamento

class DepartamentoTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_departamento_creation(self):
        departamento= Departamento()
        departamento.nombre = "Matematicas"
        
        self.assertIsNotNone(departamento)
        self.assertIsNotNone(departamento.nombre)
        self.assertEqual(departamento.nombre, "Matematicas")
        