import unittest
import os
from flask import current_app
from app import create_app
from app.models.tipodedicacion import TipoDedicacion
from app.services import TipoDedicacionService
from app import db

class TipoDedicacionTestCase(unittest.TestCase):
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
        tipodedicacion = self.__nuevotipodedicacion()
        TipoDedicacionService.crear(tipodedicacion)
        self.assertIsNotNone(tipodedicacion)
        self.assertIsNotNone(tipodedicacion.id)
        self.assertGreaterEqual(tipodedicacion.id,1)
        self.assertEqual(tipodedicacion.nombre, "Dedicacion Completa")
        self.assertEqual(tipodedicacion.observacion, "Observacion de prueba")

    def test_busqueda(self):
        tipodedicacion = self.__nuevotipodedicacion()
        TipoDedicacionService.crear(tipodedicacion)
        r=TipoDedicacionService.buscar_por_id(tipodedicacion.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Dedicacion Completa")
        self.assertEqual(r.observacion, "Observacion de prueba")
    
    def test_buscar_todos(self):
        tipodedicacion1 = self.__nuevotipodedicacion()
        tipodedicacion2 = self.__nuevotipodedicacion("Dedicacion Completa 2", "Observacion de prueba 2")
        TipoDedicacionService.crear(tipodedicacion1)
        TipoDedicacionService.crear(tipodedicacion2)
        dedicaciones = TipoDedicacionService.buscar_todos()
        self.assertIsNotNone(dedicaciones)
        self.assertEqual(len(dedicaciones), 2)

    def test_actualizar(self):
        tipodedicacion = self.__nuevotipodedicacion()
        TipoDedicacionService.crear(tipodedicacion)
        tipodedicacion.nombre = "Dedicacion actualizada"
        tipodededicacion_actualizado = TipoDedicacionService.actualizar(tipodedicacion.id ,tipodedicacion)
        self.assertEqual(tipodededicacion_actualizado.nombre, "Dedicacion actualizada")

    def test_borrar(self):
        tipodedicacion = self.__nuevotipodedicacion()
        TipoDedicacionService.crear(tipodedicacion)
        TipoDedicacionService.borrar_por_id(tipodedicacion.id)
        resultado = TipoDedicacionService.buscar_por_id(tipodedicacion.id)
        self.assertIsNone(resultado)

    def __nuevotipodedicacion(self , nombre= "Dedicacion Completa", observacion= "Observacion de prueba"):
        tipodedicacion = TipoDedicacion()
        tipodedicacion.nombre = "Dedicacion Completa"
        tipodedicacion.observacion = "Observacion de prueba"
        return tipodedicacion
        