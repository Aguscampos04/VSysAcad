import unittest
import os
from flask import current_app
from app import create_app
from app.models.grupo import Grupo
from app.services import GrupoService
from app import db

class GrupoTestCase(unittest.TestCase):
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

    def test_grupo_creation(self):
        grupo = self.__nuevogrupo()
        self.assertIsNotNone(grupo)
        self.assertIsNotNone(grupo.nombre)
        self.assertEqual(grupo.nombre, "Grupo A")

    def test_busqueda(self):
        grupo = self.__nuevogrupo()
        GrupoService.crear(grupo)
        r=GrupoService.buscar_por_id(grupo.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Grupo A")
        
    def test_buscar_todos(self):
        grupo1 = self.__nuevogrupo()
        grupo2 = self.__nuevogrupo()
        GrupoService.crear(grupo1)
        GrupoService.crear(grupo2)
        grupos = GrupoService.buscar_todos()
        self.assertIsNotNone(grupos)
        self.assertEqual(len(grupos), 2)
        
    def test_actualizar(self):
        grupo = self.__nuevogrupo()
        GrupoService.crear(grupo)
        grupo.nombre = "Grupo B"
        grupo_actualizado = GrupoService.actualizar(grupo.id, grupo)
        self.assertEqual(grupo_actualizado.nombre, "Grupo B")

    def test_borrar(self):
        grupo = self.__nuevogrupo()
        GrupoService.crear(grupo)
        GrupoService.borrar_por_id(grupo.id)
        resultado = GrupoService.buscar_por_id(grupo.id)
        self.assertIsNone(resultado)

    def __nuevogrupo(self):
        grupo = Grupo()
        grupo.nombre = "Grupo A"
        return grupo
        