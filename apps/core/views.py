from django.shortcuts import render
from apps.personas.models import Persona, P04
from django.http import JsonResponse
from django.views import View
from apps.core.models import Municipios
from django.views.generic import TemplateView
from apps.personas.models import Modalidad
from apps.core.models import Programas_formacion
from apps.core.models import Nivel_formacion
from django.db.models import Count
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

def Programa_index(request):
    modalidad = Modalidad.modalidad.field.choices
    programa_formacion_choices = Programas_formacion.Programas_formacion_choices.choices
    nivel_formacion = Nivel_formacion.Nivel_formacion_choices.choices
    context = {
        'modalidad': modalidad,
        'programa_formacion': programa_formacion_choices,
        'nivel_formacion':nivel_formacion
    }
    return render(request, 'Programa/programa.html', context)




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
            programas = P04.objects.filter(nombre_municipio_curso=nombre_municipio).values_list('nombre_programa_formacion', flat=True).distinct()
            programas_lista = list(programas)
        
        
        cantidad_de_programas =  len(programas_lista)
    
        
        context = self.get_context_data(programas_lista=programas_lista,municipio=municipio,cantidad_de_programas=cantidad_de_programas)
        return self.render_to_response(context)

#PROGRAMA


    
from django.views.generic import TemplateView
from django.db.models import Count
import json
class Programa(TemplateView):
    template_name = 'Programa/programa.html'
    
    def get(self, request, *args, **kwargs):
        selected_nivel_formacion = request.GET.get('nivel_formacion')
        selected_programa_formacion = request.GET.get('programa_formacion')
        selected_modalidad = request.GET.get('modalidad')
        selected_identificador_ficha = request.GET.get('identificador_ficha')  # Nuevo filtro
        
        filtros_programa = {}



       
        fichas = P04.objects.all()

        if selected_nivel_formacion:
            filtros_programa['nivel_formacion'] = selected_nivel_formacion
        
        # Filtrar por programa_formacion solo si ya se seleccionó nivel_formacion
        if selected_programa_formacion and selected_nivel_formacion:
            filtros_programa['nombre_programa_formacion'] = selected_programa_formacion
        
        if selected_modalidad and selected_programa_formacion:
            filtros_programa['modalidad_formacion'] = selected_modalidad
            
        
        lista_filtros = P04.objects.filter(**filtros_programa)
        
        
        

        municipios_filtro = lista_filtros.values('nombre_municipio_curso').annotate(programa_count=Count('nombre_programa_formacion')).order_by('nombre_municipio_curso')
        fichas_filtro = lista_filtros.values('identificador_ficha').order_by('identificador_ficha')
        
       
        
       
        context = self.get_context_data(
            nivel_formacion=Nivel_formacion.Nivel_formacion_choices.choices,
            programa_formacion=Programas_formacion.Programas_formacion_choices.choices,
            modalidad=Modalidad.Modalidad_choices.choices,
            
            #Mantiene la opcion en el select
            selected_nivel_formacion=selected_nivel_formacion,
            selected_programa_formacion=selected_programa_formacion,
            selected_modalidad=selected_modalidad,
            
            lista_municipios=municipios_filtro,
            lista_fichas = fichas_filtro,
           
          
            
        )
      
            
        return self.render_to_response(context)

from django.shortcuts import render, get_object_or_404
def detalle_ficha(request, identificador_ficha):
   
    ficha = get_object_or_404(P04, identificador_ficha=identificador_ficha)
    data = {
        'identificador_ficha': ficha.identificador_ficha,
        'campo1': ficha.modalidad_formacion,
        'campo2': ficha.nombre_centro,
        'campo3': ficha.tipo_de_formacion,
        'campo4': ficha.fecha_inicio_ficha,
        'campo5': ficha.fecha_terminacion_ficha,
        'campo6': ficha.red,
        'campo7': ficha.nombre_municipio_curso,
        
    }
    print(f'sdfgsdgsd{data}')
    return JsonResponse(data)