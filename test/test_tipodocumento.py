import unittest
import os
from flask import current_app
from app import create_app
from app.models.tipodocumento import TipoDocumento

class TipoDocumentoTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_tipodocumento_creation(self):
        tipodocumento = TipoDocumento()
        tipodocumento.nombre = "DNI"
        tipodocumento.libreta_civica = "12345678"
        tipodocumento.libreta_enrolamiento = "87654321"
        tipodocumento.pasaporte = "AB123456"
        self.assertIsNotNone(tipodocumento)
        self.assertIsNotNone(tipodocumento.nombre)
        self.assertEqual(tipodocumento.nombre, "DNI")
        self.assertEqual(tipodocumento.libreta_civica, "12345678")
        self.assertEqual(tipodocumento.libreta_enrolamiento, "87654321")