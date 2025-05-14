from dataclasses import dataclass 

@dataclass(init=False, repr=True, eq=True)
class Departamento():
    nombre: str