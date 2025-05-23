import unittest
import os
from flask import current_app
from app import create_app
from app.models.categoriacargo import CategoriaCargo
from app.services import CategoriaCargoService
from app import db

class CategoriaCargoTestCase(unittest.TestCase):
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

    def test_categoriacargo_creation(self):
        categoria = self.__nuevacategoria()
        self.assertIsNotNone(categoria)
        self.assertIsNotNone(categoria.nombre)
        self.assertEqual(categoria.nombre, "Docente")

    def test_crear(self):
        categoria = self.__nuevacategoria()
        CategoriaCargoService.crear(categoria)
        self.assertIsNotNone(categoria)
        self.assertIsNotNone(categoria.id)
        self.assertGreaterEqual(categoria.id, 1)
        self.assertEqual(categoria.nombre, "Docente")

    def test_busqueda(self):
        categoria = self.__nuevacategoria()
        CategoriaCargoService.crear(categoria)
        r=CategoriaCargoService.buscar_por_id(categoria.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Docente")
        
    
    def test_buscar_todos(self):
        categoria1 = self.__nuevacategoria()
        categoria2 = self.__nuevacategoria()
        CategoriaCargoService.crear(categoria1)
        CategoriaCargoService.crear(categoria2)
        categorias = CategoriaCargoService.buscar_todos()
        self.assertIsNotNone(categorias)
        self.assertEqual(len(categorias), 2)

    def test_actualizar(self):
        categoria = self.__nuevacategoria()
        CategoriaCargoService.crear(categoria)
        categoria.nombre = "Docente actualizado"
        categoria_actualizado = CategoriaCargoService.actualizar(categoria.id, categoria)
        self.assertEqual(categoria_actualizado.nombre, "Docente actualizado")

    def test_borrar(self):
        categoria = self.__nuevacategoria()
        CategoriaCargoService.crear(categoria)
        CategoriaCargoService.borrar_por_id(categoria.id)
        resultado = CategoriaCargoService.buscar_por_id(categoria.id)
        self.assertIsNone(resultado)

    def __nuevacategoria(self):
        categoria= CategoriaCargo()
        categoria.nombre = "Docente"
        return categoria
    
    
        