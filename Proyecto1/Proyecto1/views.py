from django.http import HttpResponse
import datetime
from django.template import Template, Context
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
def saludo(request): #primera vista
    p1 = Persona('Juanito', 'Perez')
    #nombre = 'Juan'
    #apellido = 'Gallardo'
    ahora = datetime.datetime.now()
    doc_externo = open('E:/Madelein/Cursos/Django/Proyecto1/Proyecto1/plantillas/miplantilla.html')
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({'nombre_persona': p1.nombre, 'apellido_persona': p1.apellido, 'momento_actual': ahora, 'temas':['Plantillas', 'Modelos', 'Formularios', 'Vistas', 'Despliegue']})
    documento = plantilla.render(ctx)
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse('Chau made')

def dameFecha(request):
    fecha_actual = datetime.datetime.now()
    documento = '<html><body><h1>Fecha y hora actual %s </h1></body></html>' % fecha_actual
    return HttpResponse(documento)

def calculaEdad(request,edad,year):
    
    periodo = year -2021
    edadFutura = edad + periodo
    documento = '<html><body><h2>En el año %s tendras %s años</h2></body></html>'%(year, edadFutura)
    return HttpResponse(documento)