from dataclasses import dataclass
from datetime import date
from app.models.tipodocumento import TipoDocumento

@dataclass(init=False, repr=True, eq=True)
class Alumno():
    nombre: str
    apellido: str
    nrodocumento: str
    tipo_documento: TipoDocumento
    fecha_nacimiento: str
    sexo: str # 'M' para masculino, 'F' para femenino
    nro_legajo: int
    fecha_ingreso: date