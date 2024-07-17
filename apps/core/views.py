from django.shortcuts import render
from apps.personas.models import P04, Formacion,Meta,Persona
from django.http import JsonResponse
from apps.core.models import Municipio,Regional,Centro_de_formacion
from apps.core.forms import Form_meta
from django.views.generic import TemplateView, CreateView
from apps.personas.models import Modalidad
from apps.core.models import Programas_formacion,Nivel_formacion
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.db.models import Count,Sum
from datetime import datetime
from django.urls import reverse_lazy
#redirecciones a las vistas
def menu(request):
    return render(request,'home.html')

def inicio_sesion(request):
    return render(request,'inicio_sesion.html')

def registro(request):
    return render(request, 'registro.html')


def Desercion_index(request):
    municipio = Municipio.nombre.field.choices
    regional = Regional.regional.field.choices
    centro_de_formacion = Centro_de_formacion.Centro_de_formacion_choices.choices
    modalidad = Modalidad.Modalidad_choices.choices
    
    context = {
        'municipio':municipio,
        'regional': regional,
        'centro_de_formacion' : centro_de_formacion,
        'modalidad': modalidad
    }
    return render(request, 'Desercion/desercion.html', context)

def estrategias(request):
    return render(request, 'Estrategias/estrategias.html')

def estrategias_institucionales(request):
    return render(request, 'Estrategias_institucionales/estrategias_institucionales.html')

def formacion_regular(request):
    return render(request, 'Formacion_regular/formacion_regular.html')

def general(request):
    return render(request, 'General/general.html')



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




#FUNCIONALIDADES

#COBERTURA

def cobertura(request):
    municipio = Municipio.nombre.field.choices
    return render(request, 'Cobertura/cobertura.html', {'municipio':municipio})

class Cobertura_mapa(TemplateView):
    template_name = 'Cobertura/cobertura.html'
    
    def get(self, request, *args, **kwargs):
        nombre_municipio = request.GET.get('nombre_municipio', None)
        programas_lista = []
        municipio = Municipio.nombre.field.choices

        if nombre_municipio:
            programas = P04.objects.filter(nombre_municipio_curso=nombre_municipio).values_list('nombre_programa_formacion', flat=True).distinct()
            programas_lista = list(programas)
        
        
        cantidad_de_programas =  len(programas_lista)
    
        
        context = self.get_context_data(programas_lista=programas_lista,municipio=municipio,cantidad_de_programas=cantidad_de_programas)
        return self.render_to_response(context)

#PROGRAMA
class Programa(TemplateView):
    template_name = 'Programa/programa.html'
    
    def get(self, request, *args, **kwargs):
        selected_nivel_formacion = request.GET.get('nivel_formacion')
        selected_programa_formacion = request.GET.get('programa_formacion')
        selected_modalidad = request.GET.get('modalidad')
       
        
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


#detalle de la ficha seleccionada
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

from datetime import datetime, date
class Desercion(TemplateView):
    template_name = 'Desercion/desercion.html'
    
    
    def get(self, request, *args, **kwargs):
        
        #deserciones
        resultado_activo = P04.objects.aggregate(total_aprendices=Sum('total_aprendices_activos'))
        resultado_total = P04.objects.aggregate(total_aprendices=Sum('total_aprendices'))
        
        aprendices_activos = int(resultado_activo['total_aprendices'])
        total_aprendices = int(resultado_total['total_aprendices'])
        deserciones = total_aprendices - aprendices_activos
       
        
        select_modalidad = request.GET.get('modalidad')
        select_municipio = request.GET.get('municipio')
        select_regional = request.GET.get('regional')
        select_centro_de_formacion = request.GET.get('centro_de_formacion')
        select_fecha_inicio_ficha = request.GET.get('fecha_inicio_ficha')
        select_fecha_terminacion_ficha = request.GET.get('fecha_terminacion_ficha')
        
      
       
       
        filtros_desercion = {}
        
       
            
        if not select_fecha_inicio_ficha:
            select_fecha_inicio_ficha = date.today().strftime('%Y-%m-%d')
        
        # Convertir la fecha de inicio a formato de fecha y aplicar filtro mayor o igual
        fecha_inicio = datetime.strptime(select_fecha_inicio_ficha, '%Y-%m-%d').date()
        filtros_desercion['fecha_inicio_ficha__gte'] = fecha_inicio

        # Si se proporciona fecha de terminación, convertirla a formato de fecha y aplicar filtro menor o igual
        if select_fecha_terminacion_ficha:
            fecha_fin = datetime.strptime(select_fecha_terminacion_ficha, '%Y-%m-%d').date()
            filtros_desercion['fecha_inicio_ficha__lte'] = fecha_fin
        else:
            # Si no se proporciona fecha de terminación, establecerla como la fecha actual
            fecha_fin = date.today()
            filtros_desercion['fecha_inicio_ficha__lte'] = fecha_fin

        if select_modalidad and select_fecha_inicio_ficha:
            filtros_desercion['modalidad_formacion'] = select_modalidad
        if select_regional and select_modalidad:
            filtros_desercion['nombre_regional'] = select_regional
        if select_centro_de_formacion and select_regional:
            filtros_desercion['nombre_centro'] =select_centro_de_formacion;
            
        if select_municipio and select_centro_de_formacion:
      
            filtros_desercion['nombre_municipio_curso'] = select_municipio
        
        desercion_datos = P04.objects.filter(**filtros_desercion)
       
   
        context = self.get_context_data(
            
            modalidad = Modalidad.Modalidad_choices.choices,
            municipio = Municipio.Municipio_choices.choices,
            regional = Regional.Regional_choices.choices,
            centro_de_formacion = Centro_de_formacion.Centro_de_formacion_choices.choices,
            
            #mantiene la opcion 
            select_modalidad= select_modalidad,
            select_municipio=select_municipio,
            select_regional=select_regional,
            select_centro_de_formacion = select_centro_de_formacion,
            select_fecha_inicio_ficha =select_fecha_inicio_ficha,
            select_fecha_terminacion_ficha =select_fecha_terminacion_ficha,
            
            desercion_datos = desercion_datos,
            aprendices_activos=aprendices_activos,
            deserciones=deserciones,
            fecha_actual = date.today().strftime('%Y-%m-%d')
           
        )
        
        return self.render_to_response(context) 
    
def Formacion_regular_index(request):
    centro_de_formacion = Centro_de_formacion.Centro_de_formacion_choices.choices
    formacion = Formacion.Formacion_choices.choices
    modalidad = Modalidad.Modalidad_choices.choices
    persona = Persona.objects.all()
    
    
    
    context = {
        'centro_de_formacion': centro_de_formacion,
        'formacion' : formacion,
        'modalidad' : modalidad,
        'persona': persona
    } 
    
    print(f'{centro_de_formacion}')
    return render(request, 'Formacion_regular/formacion_regular.html', context)


class Meta_create(CreateView):
    model = Meta
    form_class = Form_meta
    template_name = 'Formacion_regular/formacion_regular.html'
    success_url = reverse_lazy('formacion_regular_index')
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
def meta_create(request):
         
    if request.method == 'POST':
        form= Form_meta(request.POST)
        print(f'dgdfgdfgdf{form}') 
        if form.is_valid():
            form.save()
            reversed('cores:Home')
        else:
            form = Form_meta()
    return redirect(request,'cores:formacion_regular_index',{'form':form})
    