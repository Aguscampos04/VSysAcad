from flask import Blueprint
from services import AlumnoService

certificado_bp = Blueprint('certificado', __name__)

@certificado_bp.route('/certificado/<int:id>/pdf')
def reporte_pdf(id: int):
    return AlumnoService.generar_certificado_alumno_regular(id) #TODO siguiente paso es que esto pasar a pdf

#@certificado_bp.route('/certificado/<id:int>/word')
#def reporte_word():
#    pass


