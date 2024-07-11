from django.shortcuts import render
from apps.personas.models import Persona, P04
from django.http import JsonResponse
from django.views import View
from apps.core.models import Municipios
from django.views.generic import TemplateView
from apps.core.forms import MunicipiosForm
def menu(request):
    return render(request,'home.html')

def inicio_sesion(request):
    return render(request,'inicio_sesion.html')

def registro(request):
    return render(request, 'registro.html')


def desercion(request):
    return render(request, 'Desercion/desercion.html')

def estrategias(request):
    return render(request, 'Estrategias/estrategias.html')

def estrategias_institucionales(request):
    return render(request, 'Estrategias_institucionales/estrategias_institucionales.html')

def formacion_regular(request):
    return render(request, 'Formacion_regular/formacion_regular.html')

def general(request):
    return render(request, 'General/general.html')

def poblacion_vulnerable(request):
    return render(request, 'Poblacion_vulnerable/poblacion_vulnerable.html')

def programa(request):
    return render(request, 'Programa/programa.html')




def recuperar_contraseña(request):
    return render(request, 'recuperar_contraseña.html')
def grafica(request):
    return render(request, 'Estrategias/grafica.html')




def administrador(request):
    return render(request, 'administrador.html')

def Crear_metas_formacion(request):
    return render(request, 'Estrategias_institucionales/crear_meta_formacion.html')



#COBERTURA

def cobertura(request):
    municipio = Municipios.nombre.field.choices
    return render(request, 'Cobertura/cobertura.html', {'municipio':municipio})

class Cobertura_mapa(TemplateView):
    template_name = 'Cobertura/cobertura.html'
    
    def get(self, request, *args, **kwargs):
        nombre_municipio = request.GET.get('nombre_municipio', None)
        programas_lista = []
        municipio = Municipios.nombre.field.choices

        if nombre_municipio:
            programas = P04.objects.filter(nombre_municipio_curso=nombre_municipio).values_list('nombre_programa_formacion', flat=True)
            programas_lista = list(programas)
        
        context = self.get_context_data(programas_lista=programas_lista,municipio=municipio)
        return self.render_to_response(context)

 