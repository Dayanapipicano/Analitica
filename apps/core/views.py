from django.forms import BaseModelForm
from django.shortcuts import render
from apps.personas.models import P04,Meta,Persona,Modalidad,Metas_formacion,Estrategia, Estrategia_detalle,Rol
from django.http import HttpRequest, HttpResponse, JsonResponse
from apps.core.models import Municipio,Regional,Centro_de_formacion
from apps.core.forms import Form_meta, Form_meta_formacion, Form_estrategias, Form_meta_estrategia_detalle,Form_modalidad
from django.views.generic import TemplateView, CreateView, UpdateView
from apps.core.models import Programas_formacion,Nivel_formacion
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView,DeleteView
from django.db.models import Count,Sum
from datetime import datetime
from django.urls import reverse_lazy
from .serializers import MetaSerializer,EstrateiaSerializer
from django.utils import timezone
from apps.personas.models import Rol,Persona_rol
from apps.personas.decorators import permission_required
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
    modalidad = Modalidad.objects.all()
    
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
import json
def general(request):
    
    filtro_modalidad = 'PRESENCIAL'
    data =  P04.objects.filter(modalidad_formacion=filtro_modalidad)
    
    filtro_modalidad = 'VIRTUAL'
    data_virtual =  P04.objects.filter(modalidad_formacion=filtro_modalidad)
    
  
    niveles_habilitados = {
        'CURSO ESPECIAL' : 0,
        'TECNÓLOGO' : 0,
        'TÉCNICO' : 0,
        'AUXILIAR' : 0,
        'OPERARIO' : 0,
        'EVENTO' : 0
    }
    niveles_habilitados_virtual = {
        'CURSO ESPECIAL' : 0,
        'TECNÓLOGO' : 0,
        'TÉCNICO' : 0,
        'AUXILIAR' : 0,
        'OPERARIO' : 0,
        'EVENTO' : 0
    }
    
    #PRESENCIAL
    for aprendiz in data:
        activos = aprendiz.total_aprendices_activos
        nivel = aprendiz.nivel_formacion
        
        if nivel in niveles_habilitados:
            niveles_habilitados[nivel] += activos
            
    #PRESENCIAL
    for aprendiz in data_virtual:
        activos = aprendiz.total_aprendices_activos
        nivel = aprendiz.nivel_formacion
        
        if nivel in niveles_habilitados_virtual:
            niveles_habilitados_virtual[nivel] += activos
    
   
    
    labels_presenciales = [f'{nivel} Presencial' for nivel in  niveles_habilitados.keys()] 
    labels_virtuales = [f'{nivel} Virtual' for nivel in  niveles_habilitados_virtual.keys()]
    data_values = list(niveles_habilitados.values())
    data_values_virtual = list(niveles_habilitados_virtual.values())
    data =data_values + data_values_virtual
    context = {
        'labels_presenciales':json.dumps(labels_presenciales),
        'labels_virtuales':json.dumps(labels_virtuales),
        'data':data,
        
    }

    print(data)
 

    return render(request, 'General/general.html', context)



def Programa_index(request):
    modalidad = Modalidad.objects.all()
    programa_formacion_choices = Programas_formacion.Programas_formacion_choices.choices
    nivel_formacion = Nivel_formacion.Nivel_formacion_choices.choices
    context = {
        'modalidad': modalidad,
        'programa_formacion': programa_formacion_choices,
        'nivel_formacion':nivel_formacion
    }
    return render(request, 'Programa/programa.html', context)





def grafica(request):
    return render(request, 'Estrategias/grafica.html')



@permission_required('can_view_admin_dashboard')
def administrador(request):
    personas = Persona.objects.all()
    roles = Rol.objects.all()

    return render(request, 'administrador.html', {'personas': personas, 'roles':roles})




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
            modalidad=Modalidad.objects.all(),
            
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
            
            modalidad = Modalidad.objects.all(),
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
    


#FORMACION REGULAR 

def Formacion_regular_index(request):
    form = Form_meta
    form_meta_formacion = Form_meta_formacion

    
    context = {
        'form':form,
        'form_meta_formacion' : form_meta_formacion,

        
    }
    return render(request, 'Formacion_regular/formacion_regular.html', context)


class Meta_create(CreateView):
    model = Meta
    form_class = Form_meta
    template_name = 'Formacion_regular/formacion_regular.html'
    success_url = reverse_lazy('cores:formacion_regular_index') 
    
   
    def form_valid(self, form):
        user = self.request.user
        persona = Persona.objects.get(per_documento=user.per_documento)
  
        response = super().form_valid(form)
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            metas = Meta.objects.all()
            meta_options = [{'met_id': meta.met_id} for meta in metas]
            return JsonResponse({'success': True, 'options': meta_options,'message': 'Guardado exitosamente'})
        else:
            return response

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
           
            return JsonResponse({'success': False, 'errors': form.errors})
        else:
            return super().form_invalid(form)

class Meta_formacion_create(CreateView):
    model = Metas_formacion
    form_class = Form_meta_formacion
    template_name = 'Formacion_regular/formacion_regular.html'
    success_url = reverse_lazy('cores:formacion_regular_index') 
    
    
#ESTRATEGIAS_INSTITUCIONALES
def Estrategias_institucionales_index(request):
    form_estrategias_institucionales  = Form_estrategias
    form_meta = Form_meta
    form_meta_estrategia_detalle = Form_meta_estrategia_detalle
    municipio = Municipio.Municipio_choices.choices
    modalidad = Modalidad.objects.all()
    estrategia =    Estrategia.objects.all()
    meta_estrategia =   Estrategia_detalle.objects.all()

  

    
    

    context = {
        'form_estrategias_institucionales':form_estrategias_institucionales,
        'form_meta':form_meta,
        'form_meta_estrategia_detalle': form_meta_estrategia_detalle,
        'municipio':municipio,
        'modalidad':modalidad,
        'estrategia':estrategia,
        'detalle_estrategia':meta_estrategia,



    }
    
    return render(request, 'Estrategias_institucionales/estrategias_institucionales.html', context)

class Estrategias_create(CreateView):
    model = Estrategia
    form_class = Form_estrategias
    template_name = 'Estrategias_institucionales/estrategias_institucionales'
    success_url = reverse_lazy('cores:estrategias_institucionales_index')
    
    

def get_meta_valores(request,met_id):
    
    
    try:
        meta = get_object_or_404(Meta, met_id=met_id)
        data = {
            'met_total_otras_poblaciones': meta.met_total_otras_poblaciones,
            'met_total_victimas' : meta.met_total_victimas,
            'met_total_hechos_victimizantes' : meta.met_total_hechos_victimizantes,
            'met_total_desplazados_violencia' :meta.met_total_desplazados_violencia,
            'met_total_titulada': meta.met_total_titulada,
            'met_total_complementaria': meta.met_total_complementaria,
            'met_total_poblacion_vulnerable': meta.met_total_poblacion_vulnerable,
            
            
   
        
        }
        
        

    
        return JsonResponse(data)
    except Meta.DoesNotExist:
        return JsonResponse({'error': 'Meta not found'},  status=404)


#funciones de meta estrategia, vista estrategias institucionales
from django.http import HttpResponseRedirect
#crear meta estrategia detalle
class Meta_estrategia_detalle(CreateView):
    model = Estrategia_detalle
    form_class = Form_meta_estrategia_detalle
    template_name = 'Estrategias_institucionales/estrategias_institucionales.html'
    success_url = reverse_lazy('cores:estrategias_institucionales_index')
    
    
    #recibe los datos seleccionados
    def post(self, request, *args, **kwargs):
        
        
        
        form = self.get_form()
        print('Contenido del POST:', request.POST)
        
        

        est_id = request.POST.get('est_id')
        estd_meta = request.POST.get('estd_meta')
   
        
        meta_id = int(estd_meta)
       
        

        
       
        form.fields['est_id'].queryset = Estrategia.objects.filter(est_id=est_id)
        form.fields['estd_meta'].initial = meta_id 
     

        if form.is_valid():
               return self.form_valid(form)
        else:
            print('errr', form.errors)
            return self.form_invalid(form)
        

 

   
     

     

#filtros de estrategias 
def get_estrategia_data(request,id_estd_modalidad):

        estrategia = Estrategia.objects.filter(est_modalidad=id_estd_modalidad)


        data = {
        'estrategia': [
            {
                'estrategia_id': e.est_id,
                'estrategia_nombre': e.est_nombre,
            } for e in estrategia
        ]
       }
        
        return JsonResponse(data)
    
#datos para los filtros de meta_estrategia
def meta_data(request,id_estrategia):
    estrategia = Estrategia.objects.get(est_id=id_estrategia)
    
    metas = estrategia.met_id
    meta_serializer = MetaSerializer(metas)
    data = {
        'meta': meta_serializer.data
    }
    return JsonResponse(data)
    
#detalle meta estrategias institucionales

def meta_detalle(request, estd_meta):
    try:
        meta = Meta.objects.get(met_id=estd_meta)
        data = {
            'met_codigo': meta.met_codigo,
            'met_centro_formacion' :meta.met_centro_formacion,
            'met_fecha_inicio' : meta.met_fecha_inicio,
            'met_fecha_fin': meta.met_fecha_fin,
            'met_año' : meta.met_año,
            
        }
        print(data)
        return JsonResponse(data)
    except Meta.DoesNotExist:
        return JsonResponse({'Error':'Meta not found'}, status=404)
    

#filtros para gestion formacion



class metas_formacion_filtros(TemplateView):
    model = Metas_formacion
    template_name = 'Formacion_regular/formacion_regular.html'

    def get(self, request, *args, **kwargs):
        fecha_inicio = request.GET.get('fecha_inicio')
        fecha_fin = request.GET.get('fecha_fin')
        modalidad = request.GET.get('modalidad')
        ano = request.GET.get('ano')

        filtros_formacion = {}

        if fecha_inicio:
            try:
                fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
                filtros_formacion['met_id__met_fecha_fin__gte'] = fecha_inicio
            except ValueError:
                return JsonResponse({'error': 'Fecha de inicio inválida'}, status=400)

        if fecha_fin:
            try:
                fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d')
                filtros_formacion['met_id__met_fecha_inicio__lte'] = fecha_fin
            except ValueError:
                return JsonResponse({'error': 'Fecha de fin inválida'}, status=400)

        if modalidad:
            filtros_formacion['metd_modalidad'] = modalidad

        if ano:
            filtros_formacion['met_id__met_año'] = ano

        if fecha_inicio or fecha_fin:
            modalidades = Metas_formacion.objects.filter(**filtros_formacion).values_list('metd_modalidad', 'metd_modalidad__modalidad').distinct()
        else:
            modalidades = Modalidad.objects.all().values_list('id', 'modalidad')        

        # Filtrar datos según los filtros aplicados
        resultados = Metas_formacion.objects.filter(**filtros_formacion).values(
            'metd_modalidad__modalidad',
            'met_formacion_operario',
            'met_formacion_auxiliar',
            'met_formacion_tecnico',
            'met_formacion_profundizacion_tecnica',
            'met_formacion_tecnologo',
            'met_formacion_evento',
            'met_formacion_curso_especial',
            'met_formacion_bilinguismo',
            'met_formacion_sin_bilinguismo',
            'met_id__met_codigo',
            'met_id__met_centro_formacion',
            'met_id__met_fecha_inicio',
            'met_id__met_fecha_fin',
            'met_id__met_año',
        )

        data = {
            'modalidades': list(modalidades),
            'data': list(resultados)
        }
        return JsonResponse(data)

class estrategias_institucionales_filtros(TemplateView):
    model = Estrategia_detalle
    template_name = 'Estrategias_institucionales/estrategias_institucionales.html'

    def get(self, request, *args, **kwargs):
        fecha_inicio = request.GET.get('fecha_inicio')
        fecha_fin = request.GET.get('fecha_fin')
        modalidad = request.GET.get('modalidad')
        año = request.GET.get('año')
        

        estrategia_detalle_filtro = {}
        

        if fecha_inicio:
            fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
        if fecha_fin:
            fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d')
            
        if fecha_inicio and fecha_fin:
            id_meta_filtrados = Meta.objects.filter(met_fecha_inicio__gte=fecha_inicio, met_fecha_fin__lte=fecha_fin).values_list('met_id', flat=True)
        elif fecha_inicio:
            id_meta_filtrados = Meta.objects.filter(met_fecha_inicio__gte=fecha_inicio).values_list('met_id',flat=True)
    
        elif fecha_fin:
            id_meta_filtrados = Meta.objects.filter(met_fecha_fin__lte=fecha_fin).values_list('met_id',flat=True)
        
        else:
            id_meta_filtrados = []
     
        if id_meta_filtrados:
               estrategia_detalle_filtro['estd_meta__in'] = id_meta_filtrados
               
              
       
            
        
        if fecha_inicio or fecha_fin:
            modalidades = Estrategia_detalle.objects.filter(**estrategia_detalle_filtro).values_list('estd_modalidad', 'estd_modalidad').distinct()
 
        else:
            modalidades = Modalidad.objects.all().values_list('id', 'modalidad')        
        if modalidad:
            estrategia_detalle_filtro['estd_modalidad'] = modalidad
            
        if año:
            id_metas_año = Meta.objects.filter(met_año=año).values_list('met_id', flat=True)
            estrategia_detalle_filtro['estd_meta__in'] = id_metas_año
            print('fdsfdsfsdmeta',estrategia_detalle_filtro)
        
       

            
   

 

        # Filtrar datos según los filtros aplicados
        resultados = Estrategia_detalle.objects.filter(**estrategia_detalle_filtro).values(
            'estd_id',
            'estd_modalidad',
            'est_id__est_nombre',
            'estd_operario_meta',
            'estd_auxiliar_meta',
            'estd_tecnico_meta',
            'estd_profundizacion_tecnica_meta',
            'estd_tecnologo',
            'estd_tecnico_meta',
            'estd_evento',
            'estd_curso_especial',
            'estd_bilinguismo',
            'estd_sin_bilinguismo',
            'est_id__est_total_meta',
            'estd_meta',
        )
        

        
       
        

        data = {
            'modalidades': list(modalidades),
            'data': list(resultados)
        }
        return JsonResponse(data)
#CRUD MODALIDAD

def Modalidad_index(request):
    view_modalidades = Modalidad.objects.all()
    form_modalidad = Form_modalidad
    
    context = {
         'view_modalidades':view_modalidades,
         'form_modalidad':form_modalidad,
    }
    
    return render(request, 'Modalidad/modalidad_list.html',context)
class Modalidad_create(CreateView):
    model =  Modalidad
    form_class = Form_modalidad
    template_name = 'Modalidad/modalidad_index.html'
    success_url = reverse_lazy('cores:modalidad_index')

class Modalidad_delete(DeleteView):
    model = Modalidad
    success_url = reverse_lazy('cores:modalidad_index')

class Modalidad_edit(UpdateView):
    model = Modalidad
    from_class = Form_modalidad
    fields = ['modalidad']
    success_url = reverse_lazy('cores:modalidad_index')
    
    
#ROLES

def Asignacion_roles(request):
    if request.method == 'POST':
        persona_id = request.POST.get('persona_id')
        rol_id = request.POST.get('rol_id')

        persona = get_object_or_404(Persona, per_documento=persona_id)
        nuevo_rol = get_object_or_404(Rol, rol_id=rol_id)

        # Elimina todos los roles actuales de la persona
        Persona_rol.objects.filter(persona_id=persona).delete()

        # Asigna el nuevo rol a la persona
        Persona_rol.objects.create(persona_id=persona, rol_id=nuevo_rol, rolp_fecha_inicio=timezone.now(),rolp_fecha_fin=timezone.now())

        return redirect('administrador')
    else:
        return redirect('administrador') 