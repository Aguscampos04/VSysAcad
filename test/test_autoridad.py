import unittest
import os
from flask import current_app
from app import create_app, db
from app.models.autoridad import Autoridad
from app.models.cargo import Cargo
from test.instancias import nuevocargo, nuevamateria
from app.services import AutoridadService


#TODO hay que hacer la relacion muchos a muchos con materia
class AutoridadTestCase(unittest.TestCase):
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
        autoridad = self.__nuevaautoridad()
        AutoridadService.crear(autoridad)
        self._assert_autoridad(autoridad, "Pelo","123456789","123@gmail.com")
        self.assertIsNotNone(autoridad.email)
        self.assertIsNotNone(autoridad.materias)

    def test_busqueda(self):
        autoridad = self.__nuevaautoridad()
        AutoridadService.crear(autoridad)
        r=AutoridadService.buscar_por_id(autoridad.id)
        self._assert_autoridad(r, "Pelo", "123456789", "123@gmail.com")        
        self.assertIsNotNone(r.email)
        self.assertIsNotNone(r.materias)
    
    def test_buscar_todos(self):
        autoridad1 = self.__nuevaautoridad()
        autoridad2 = self.__nuevaautoridad(nombre="Pato", cargo=None,telefono="12345678",email="124@gmail.com")
        AutoridadService.crear(autoridad1)
        AutoridadService.crear(autoridad2)
        autoridades = AutoridadService.buscar_todos()
        self._assert_autoridad(autoridades[0], "Pelo","123456789","123@gmail.com")
        self._assert_autoridad(autoridades[1], "Pato","12345678","124@gmail.com")
        self.assertEqual(len(autoridades), 2)

    def test_actualizar(self):
        autoridad = self.__nuevaautoridad()
        AutoridadService.crear(autoridad)
        autoridad.nombre = "Decano"
        autoridad_actualizada = AutoridadService.actualizar(autoridad.id,autoridad)
        self.assertEqual(autoridad_actualizada.nombre, "Decano")

    def test_borrar(self):
        autoridad = self.__nuevaautoridad()
        AutoridadService.crear(autoridad)
        AutoridadService.borrar_por_id(autoridad.id)
        resultado = AutoridadService.buscar_por_id(autoridad.id)
        self.assertIsNone(resultado)


    def test_autoridad_con_materias(self):
        autoridad = self.__nuevaautoridad()
        AutoridadService.crear(autoridad)
        autoridad_db = AutoridadService.buscar_por_id(autoridad.id)
        self.assertEqual(len(autoridad_db.materias), 1)
        self.assertEqual(autoridad_db.materias[0].nombre, "Matematica")


    def test_actualizar_con_materias(self):
        autoridad = self.__nuevaautoridad()
        AutoridadService.crear(autoridad)
        
        nueva_materia = nuevamateria(nombre="Algebra")

        autoridad.nombre = "vice-Decano"
        autoridad.materias = [nueva_materia]  
        autoridad_actualizada = AutoridadService.actualizar(autoridad.id, autoridad)

        self.assertEqual(autoridad_actualizada.nombre, "vice-Decano")
        self.assertEqual(len(autoridad_actualizada.materias), 1)
        self.assertEqual(autoridad_actualizada.materias[0].nombre, "Algebra")

    def __nuevaautoridad(self, nombre="Pelo", cargo=None, telefono="123456789", email="123@gmail.com", materias=None):
        autoridad = Autoridad()
        autoridad.nombre = nombre
        autoridad.cargo = nuevocargo()
        autoridad.telefono = telefono
        autoridad.email = email
        autoridad.materias = [nuevamateria()]
        return autoridad
    
    def _assert_autoridad(self,autoridad,nombre,telefono, email):
        self.assertIsNotNone(autoridad)
        self.assertEqual(autoridad.nombre, nombre)
        self.assertEqual(autoridad.telefono, telefono)
        self.assertEqual(autoridad.email, email)
        self.assertIsNotNone(autoridad.id)
        self.assertGreaterEqual(autoridad.id, 1)