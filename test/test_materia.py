import unittest
import os
from flask import current_app
from app import create_app
from app.models.materia import Materia
from app.services import MateriaService
from app import db


class MateriaTestCase(unittest.TestCase):
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
        materia = self.__nuevamateria()
        MateriaService.crear(materia)
        self.assertIsNotNone(materia)
        self.assertIsNotNone(materia.id)
        self.assertGreaterEqual(materia.id, 1)
        self.assertEqual(materia.nombre, "Matematicas")

    def test_busqueda(self):
        materia = self.__nuevamateria()
        MateriaService.crear(materia)
        r = MateriaService.buscar_por_id(materia.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, materia.nombre)
        self.assertEqual(r.codigo, materia.codigo)
        self.assertEqual(r.observacion, materia.observacion)

    def test_buscar_todos(self):
        materia1 = self.__nuevamateria()
        materia2 = self.__nuevamateria(
            "Historia", "HIS101", "Historia de prueba")
        MateriaService.crear(materia1)
        MateriaService.crear(materia2)
        materias = MateriaService.buscar_todos()
        self.assertIsNotNone(materias)
        self.assertEqual(len(materias), 2)

    def test_actualizar(self):
        materia = self.__nuevamateria()
        MateriaService.crear(materia)
        materia.nombre = "Matematicas Avanzadas"
        materia_actualizada = MateriaService.actualizar(materia.id, materia)
        self.assertEqual(materia_actualizada.nombre, "Matematicas Avanzadas")

    def test_borrar_por_id(self):
        materia = self.__nuevamateria()
        MateriaService.crear(materia)
        MateriaService.borrar_por_id(materia.id)
        r = MateriaService.buscar_por_id(materia.id)
        self.assertIsNone(r)

    def __nuevamateria(self, nombre="Matematicas", codigo="MAT101", observacion="Observacion de prueba"):
        materia = Materia()
        materia.nombre = nombre
        materia.codigo = codigo
        materia.observacion = observacion
        return materia
