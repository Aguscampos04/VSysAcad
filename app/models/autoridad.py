from dataclasses import dataclass
from app.models import Cargo
from app.models.relations import autoridades_materias 
from app import db

@dataclass(init=False, repr=True, eq=True)
class Autoridad(db.Model):
    __tablename__ = "autoridades"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(100), nullable=False)
    #TODO str o int?
    telefono: str = db.Column(db.String(20), nullable=True)
    email: str = db.Column(db.String(100), nullable=True)

    cargo_id: int = db.Column(db.Integer, db.ForeignKey('cargos.id'), nullable=False)
    cargo = db.relationship('Cargo',  lazy=True) 

    materias = db.relationship('Materia', secondary=autoridades_materias, back_populates='autoridades')

    def asociar_materia(self, materia):
        if materia not in self.materias:
            self.materias.append(materia)

    def desasociar_materia(self, materia):
        if materia in self.materias:
            self.materias.remove(materia)