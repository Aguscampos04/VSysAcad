import unittest
from app import create_app, db
from app.models import Autoridad, Materia
from app.services import AutoridadService, MateriaService
from test.instancias import nuevaautoridad, nuevamateria

class AutoridadTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_crear(self):
        autoridad = nuevaautoridad()
        self.assertIsNotNone(autoridad.id)
        self.assertEqual(autoridad.nombre, "Pelo")

    def test_buscar_por_id(self):
        autoridad = nuevaautoridad()
        encontrado = AutoridadService.buscar_por_id(autoridad.id)
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.nombre, autoridad.nombre)

    def test_buscar_todos(self):
        autoridad1 = nuevaautoridad(nombre="Pelo1")
        autoridad2 = nuevaautoridad(nombre="Pelo2")
        autoridades = AutoridadService.buscar_todos()
        self.assertIsNotNone(autoridades)
        self.assertGreaterEqual(len(autoridades), 2)
        nombres = [a.nombre for a in autoridades]
        self.assertIn("Pelo1", nombres)
        self.assertIn("Pelo2", nombres)

    def test_actualizar(self):
        autoridad = nuevaautoridad()
        autoridad.nombre = "Nombre Actualizado"
        actualizado = AutoridadService.actualizar(autoridad.id, autoridad)
        self.assertEqual(actualizado.nombre, "Nombre Actualizado")

    def test_borrar(self):
        autoridad = nuevaautoridad()
        borrado = AutoridadService.borrar_por_id(autoridad.id)
        self.assertTrue(borrado)
        encontrado = AutoridadService.buscar_por_id(autoridad.id)
        self.assertIsNone(encontrado)

    def test_relacion_materias(self):
        autoridad = nuevaautoridad()
        materia1 = nuevamateria(nombre="Matematica")
        materia2 = nuevamateria(nombre="Fisica")

        # Asociar materias desde autoridad.materias 
        autoridad.materias.append(materia1)
        autoridad.materias.append(materia2)
        db.session.commit()

        self.assertIn(materia1, autoridad.materias)
        self.assertIn(materia2, autoridad.materias)
        self.assertIn(autoridad, materia1.autoridades)
        self.assertIn(autoridad, materia2.autoridades)

        # Desasociar una materia
        autoridad.materias.remove(materia1)
        db.session.commit()
        self.assertNotIn(materia1, autoridad.materias)
        self.assertNotIn(autoridad, materia1.autoridades)
