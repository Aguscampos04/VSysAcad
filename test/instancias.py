from app.models import (
    Alumno, Area, Autoridad, Cargo, CategoriaCargo, Departamento,
    Especialidad, Facultad, Grado, Grupo, Materia, Orientacion,
    Plan, TipoDedicacion, TipoDocumento, TipoEspecialidad, Universidad
)
from datetime import date

def nuevotipodocumento(dni=46291002, libreta_civica="nacional", libreta_enrolamiento="naci", pasaporte="nacnal"):
    tipo_documento = TipoDocumento()
    tipo_documento.dni = dni
    tipo_documento.libreta_civica = libreta_civica
    tipo_documento.libreta_enrolamiento = libreta_enrolamiento
    tipo_documento.pasaporte = pasaporte
    return tipo_documento

def nuevotipodedicacion(nombre="Dedicacion Completa", observacion="Observacion de prueba"):
    td = TipoDedicacion()
    td.nombre = nombre
    td.observacion = observacion
    return td

def nuevacategoriacargo(nombre="Docente"):
    categoria = CategoriaCargo()
    categoria.nombre = nombre
    return categoria

def nuevocargo(nombre="Profesor", puntos=10, categoria_cargo=None, tipo_dedicacion=None):
    cargo = Cargo()
    cargo.nombre = nombre
    cargo.puntos = puntos
    cargo.categoria_cargo = categoria_cargo or nuevacategoriacargo()
    cargo.tipo_dedicacion = tipo_dedicacion or nuevotipodedicacion()
    return cargo

def nuevafacultad(nombre="Facultad de Ciencias", abreviatura="FCC", directorio="/facultad/ciencias",
                  sigla="FC", codigopostal="12345", ciudad="Ciudad", domicilio="Calle 123",
                  telefono="123456789", contacto="Juan Perez", email="1234@gmail.com"):
    facultad = Facultad()
    facultad.nombre = nombre
    facultad.abreviatura = abreviatura
    facultad.directorio = directorio
    facultad.sigla = sigla
    facultad.codigopostal = codigopostal
    facultad.ciudad = ciudad
    facultad.domicilio = domicilio
    facultad.telefono = telefono
    facultad.contacto = contacto
    facultad.email = email
    return facultad

def nuevodepartamento(nombre="Matematicas"):
    departamento = Departamento()
    departamento.nombre = nombre
    return departamento

def nuevaarea(nombre="Matematica"):
    area = Area()
    area.nombre = nombre
    return area

def nuevotipoespecialidad(nombre="Cardiologia", nivel="Avanzado"):
    tipo = TipoEspecialidad()
    tipo.nombre = nombre
    tipo.nivel = nivel
    return tipo

def nuevaespecialidad(nombre="Matematicas", letra="A", observacion="Observacion de prueba", tipoespecialidad=None):
    esp = Especialidad()
    esp.nombre = nombre
    esp.letra = letra
    esp.observacion = observacion
    esp.tipoespecialidad = tipoespecialidad or nuevotipoespecialidad()
    return esp

def nuevoplan(nombre="Plan A", fecha_inicio=date(2024, 6, 4), fecha_fin=date(2024, 6, 5), observacion="Observacion de prueba"):
    plan = Plan()
    plan.nombre = nombre
    plan.fecha_inicio = fecha_inicio
    plan.fecha_fin = fecha_fin
    plan.observacion = observacion
    return plan

def nuevamateria(nombre="Matematicas", codigo="MAT101", observacion="Observacion de prueba"):
    materia = Materia()
    materia.nombre = nombre
    materia.codigo = codigo
    materia.observacion = observacion
    return materia

def nuevaorientacion(nombre="Orientacion 1", especialidad=None, plan=None, materia=None):
    orientacion = Orientacion()
    orientacion.nombre = nombre
    orientacion.especialidad = especialidad or nuevaespecialidad()
    orientacion.plan = plan or nuevoplan()
    orientacion.materia = materia or nuevamateria()
    return orientacion

def nuevauniversidad(nombre="Universidad Nacional", sigla="UN"):
    uni = Universidad()
    uni.nombre = nombre
    uni.sigla = sigla
    return uni

def nuevogrado(nombre="Primero", descripcion="Descripcion del primer grado"):
    grado = Grado()
    grado.nombre = nombre
    grado.descripcion = descripcion
    return grado

def nuevogrupo(nombre="Grupo A"):
    grupo = Grupo()
    grupo.nombre = nombre
    return grupo

def nuevoalumno(nombre="Juan", apellido="Pérez", nrodocumento="46291002", tipo_documento=None,
                fecha_nacimiento=date(1990, 1, 1), sexo="M", nro_legajo=123456, fecha_ingreso=date(2020, 1, 1)):
    alumno = Alumno()
    alumno.nombre = nombre
    alumno.apellido = apellido
    alumno.nrodocumento = nrodocumento
    alumno.tipo_documento = tipo_documento or nuevotipodocumento()
    alumno.fecha_nacimiento = fecha_nacimiento
    alumno.sexo = sexo
    alumno.nro_legajo = nro_legajo
    alumno.fecha_ingreso = fecha_ingreso
    return alumno

def nuevaautoridad(nombre="Pelo", cargo=None, telefono="123456789", email="123@gmail.com"):
    autoridad = Autoridad()
    autoridad.nombre = nombre
    autoridad.cargo = cargo or nuevocargo()
    autoridad.telefono = telefono
    autoridad.email = email
    return autoridad
