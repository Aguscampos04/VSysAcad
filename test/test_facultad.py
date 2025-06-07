import unittest
import os
from flask import current_app
from app import create_app
from app.models.facultad import Facultad
from app.services.facultad_service import FacultadService
from app import db
from test.instancias import nuevafacultad

class FacultadTestCase(unittest.TestCase):
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
        facultad = nuevafacultad()
        self.assertIsNotNone(facultad)
        self.assertIsNotNone(facultad.id)
        self.assertIsNotNone(facultad.universidad)
        self.assertEqual(facultad.universidad.nombre,"Universidad Nacional")
        self.assertGreaterEqual(facultad.id, 1)
        self.assertEqual(facultad.nombre, "Facultad de Ciencias")

    def test_buscar_por_id(self):
        facultad = nuevafacultad()
        r=FacultadService.buscar_por_id(facultad.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Facultad de Ciencias")
        self.assertEqual(r.abreviatura, "FCC")

    def test_buscar_todos(self):
        facultad1 = nuevafacultad()
        facultad2 = nuevafacultad()
        facultades = FacultadService.buscar_todos()
        self.assertIsNotNone(facultades)
        self.assertEqual(len(facultades), 2)

    def test_actualizar(self):
        facultad= nuevafacultad()
        facultad.nombre = "Facultad de Ciencias Actualizada"
        facultad_actualizada = FacultadService.actualizar(facultad.id, facultad)
        self.assertEqual(facultad_actualizada.nombre, "Facultad de Ciencias Actualizada")

    def test_borrar(self):
        facultad = nuevafacultad()
        FacultadService.borrar_por_id(facultad.id)
        resultado = FacultadService.buscar_por_id(facultad.id)
        self.assertIsNone(resultado)
    