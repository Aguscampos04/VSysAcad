from dataclasses import dataclass

@dataclass(init=False, repr=True, eq=True)
class Especialidad():
    nombre: str
    letra: str
    observacion: str