import unittest
import os
from flask import current_app
from app import create_app
from app.models.materia import Materia
from app.services import MateriaService
from test.instancias import nuevaautoridad
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
        self.assertIsNotNone(materia.autoridades)
        self.assertGreaterEqual(materia.id, 1)
        self.assertEqual(materia.nombre, "Matematica")

    def test_busqueda(self):
        materia = self.__nuevamateria()
        MateriaService.crear(materia)
        r = MateriaService.buscar_por_id(materia.id)
        self.assertIsNotNone(r)
        self.assertIsNotNone(materia.autoridades)
        self.assertEqual(r.nombre, materia.nombre)
        self.assertEqual(r.codigo, materia.codigo)

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
        materia.nombre = "Matematica Avanzadas"
        materia_actualizada = MateriaService.actualizar(materia.id, materia)
        self.assertEqual(materia_actualizada.nombre, "Matematica Avanzadas")

    def test_borrar_por_id(self):
        materia = self.__nuevamateria()
        MateriaService.crear(materia)
        MateriaService.borrar_por_id(materia.id)
        r = MateriaService.buscar_por_id(materia.id)
        self.assertIsNone(r)

    def test_materias_con_autoridades(self):
        materia = self.__nuevamateria()
        MateriaService.crear(materia)
        materia_db = MateriaService.buscar_por_id(materia.id)
        self.assertEqual(len(materia_db.autoridades), 1)
        self.assertEqual(materia_db.autoridades[0].nombre, "Pelo")

    def test_actualizar_con_autoridades(self):
        materia = self.__nuevamateria()
        MateriaService.crear(materia)
        
        nueva_autoridad = nuevaautoridad(nombre="lengua")

        materia.nombre = "programacion"
        materia.autoridades = [nueva_autoridad]  
        materia_actualizada = MateriaService.actualizar(materia.id, materia)

        self.assertEqual(materia_actualizada.nombre, "programacion")
        self.assertEqual(len(materia_actualizada.autoridades), 1)
        self.assertEqual(materia_actualizada.autoridades[0].nombre, "lengua")

    def __nuevamateria(self, nombre="Matematica", codigo="MAT101", observacion="Observacion de prueba", autoridades =None):
        materia = Materia()
        materia.nombre = nombre
        materia.codigo = codigo
        materia.observacion = observacion
        if autoridades is None:
            autoridades = [nuevaautoridad()]
        materia.autoridades = autoridades
        return materia
