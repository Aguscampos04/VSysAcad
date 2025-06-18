from flask import render_template
from app.models import Alumno
from app.repositories import AlumnoRepository
from app.services import FacultadService, EspecialidadService
from datetime import datetime

class AlumnoService:

    @staticmethod
    def crear(alumno):
        AlumnoRepository.crear(alumno)

    @staticmethod
    def buscar_por_id(id: int) -> Alumno:        
        return AlumnoRepository.buscar_por_id(id)

    @staticmethod
    def buscar_todos() -> list[Alumno]:
        return AlumnoRepository.buscar_todos()
    
    @staticmethod
    def actualizar(id: int, alumno: Alumno) -> Alumno:
        alumno_existente = AlumnoRepository.buscar_por_id(id)
        if not alumno_existente:
            return None
        alumno_existente.nombre = alumno.nombre
        alumno_existente.apellido = alumno.apellido
        alumno_existente.nrodocumento = alumno.nrodocumento
        alumno_existente.tipo_documento = alumno.tipo_documento
        alumno_existente.fecha_nacimiento = alumno.fecha_nacimiento
        alumno_existente.sexo = alumno.sexo
        alumno_existente.nro_legajo = alumno.nro_legajo
        alumno_existente.fecha_ingreso = alumno.fecha_ingreso
        return alumno_existente
        
    @staticmethod
    def borrar_por_id(id: int) -> bool:
        return AlumnoRepository.borrar_por_id(id)
    
    #siempre se llama de service a service de otros modelos
    @staticmethod
    def generar_certificado_alumno_regular(id: int):
        alumno = AlumnoRepository.buscar_por_id(id)
        #TODO agregar relacion alumno con facultad y especialidad
        facultad = FacultadService.buscar_por_id(19) #entre parentesis se pone alumno.facultad_id
        fecha = datetime.now()
        especialidad = EspecialidadService.buscar_por_id(5)
        return render_template("certificado/certificado.html", alumno=alumno, facultad=facultad, fecha=fecha, especialidad=especialidad)