from django.shortcuts import render
from apps.personas.forms import PersonaForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from apps.personas.models import Persona
from apps.personas.forms import EditProfileForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.views import PasswordResetView
from django.http import HttpResponseRedirect
from django.contrib.auth.views import PasswordResetDoneView
from django.utils import timezone
import pandas as pd
from django.shortcuts import render
from apps.personas.models import P04
from django.utils import timezone
import numpy as np
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
#MENSAJE DE CAMBIO DE CONTRASEÑA
class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('personas:perfil') 

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, '¡Contraseña cambiada exitosamente!')
        return response

#REFIRECCION DE EL HOME
def Home(request):
    return render(request,'home.html')

#REGISTRO DE PERSONA
def Registro(request):
 
   if request.method == 'POST':
   
        formPersona = PersonaForm(request.POST)
        if formPersona.is_valid():
            formPersona.save()
            per_documento = formPersona.cleaned_data.get('per_documento')
            raw_password = formPersona.cleaned_data.get('password1')
            user = authenticate(username=per_documento, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('personas:inicio_sesion')
            else:
                print('Error en autenticación') 
        else:
            print('Errores en el formulario:', formPersona.errors) 
   else:
        formPersona = PersonaForm()
   return render(request,'registro.html',{'formPersona': formPersona})

#INICIO DE SESION DE PERSONA
def inicio_sesion(request):
    if request.method == 'POST':
        formPersona = LoginForm(request.POST)
        if formPersona.is_valid():
            per_documento = formPersona.cleaned_data['per_documento']
            password = formPersona.cleaned_data['password1']
            user = authenticate(request, per_documento=per_documento, password=password)
            if user is not None:
                login(request, user)
                return redirect('personas:Home')  # Redirigir a la página principal u otra página
            else:
                messages.error(request, 'Usuario o contraseña incorrectos')
        # Si el formulario no es válido, los errores se agregarán automáticamente al formulario
    else:
        formPersona = LoginForm()

    # No agregar mensajes de error al contexto si el formulario no se ha enviado (GET request)
    return render(request, 'inicio_sesion.html', {'formPersona': formPersona})

#CONFIRMACION DE LA EXISTENCIAS DE UN CORREO ELECTRONICO
def validacion_email(request):
    email = request.GET.get('email')
    exists = Persona.objects.filter(email=email).exists()
    return JsonResponse({'exists': exists})

def validar_documento(request):
    documento = request.GET.get('documento')
    exists = Persona.objects.filter(per_documento=documento).exists()
    return JsonResponse({'exists': exists})

#REDIRIGE AL PERFIL CON LOS DATOS EXISTENTES
def Perfil(request):
    formPersona = EditProfileForm
    return render(request, 'perfil.html',{'formPersona':formPersona})



#EDITAR PERFIL DE LA PERSONA
@login_required
def Editar_perfil(request, per_documento):
    persona = Persona.objects.get(per_documento=per_documento)
    
    if request.method == 'POST':
        formPersona = EditProfileForm(request.POST, request.FILES, instance=persona)
       
        if formPersona.is_valid():
            formPersona.save()
            return redirect(reverse('personas:editar_perfil', kwargs={'per_documento': per_documento}))
        
    else:
        formPersona = EditProfileForm(instance=persona)
        
    return render(request, 'perfil.html', {'formPersona': formPersona})


#captura el correo que se ingreso en el formulario
class CustomPasswordResetView(PasswordResetView):
    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        response = super().form_valid(form)
        return HttpResponseRedirect(f"{reverse_lazy('password_reset_done')}?email={email}")


#recibe el correo ingresado para visualizarlo
class CustomPasswordResetDoneView(PasswordResetDoneView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['email'] = self.request.GET.get('email')
        return context




def p04(request):
    per_documento = Persona.objects.all()
    
    return render(request,'p04.html',  {'per_documento':per_documento})


def subir_P04(request):
    if request.method == 'POST':
        archivo = request.FILES.get('fileUpload')
        per_documento = request.POST.get('per_documento')
      
    
        if archivo and archivo.name.endswith('.xlsx'):
            try:
                selected_persona = Persona.objects.get(per_documento=per_documento)
                df = pd.read_excel(archivo, header=4)
                df['FECHA_INICIO_FICHA'] = pd.to_datetime(df['FECHA_INICIO_FICHA'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d') 
                df['FECHA_TERMINACION_FICHA'] = pd.to_datetime(df['FECHA_TERMINACION_FICHA'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d') 
               
                df = df.replace(r'^\s*$', np.nan, regex=True)

           

                # Itera sobre las filas del DataFrame
                for index, row in df.iterrows():
                    p = P04(
                        fecha_p04=timezone.now(),
                        codigo_regional=row['CODIGO_REGIONAL'],
                        nombre_regional=row['NOMBRE_REGIONAL'],
                        codigo_centro=row['CODIGO_CENTRO'],
                        nombre_centro=row['NOMBRE_CENTRO'],
                        identificador_ficha=row['IDENTIFICADOR_FICHA'],
                        identificador_unico_ficha=row['IDENTIFICADOR_UNICO_FICHA'],
                        estado_curso=row['ESTADO_CURSO'],
                        codigo_nivel_formacion=row['CODIGO_NIVEL_FORMACION'],
                        nivel_formacion=row['NIVEL_FORMACION'],
                        codigo_jornada=row['CODIGO_JORNADA'],
                        nombre_jornada=row['NOMBRE_JORNADA'],
                        tipo_de_formacion=row['TIPO_DE_FORMACION'],
                        fecha_inicio_ficha = row['FECHA_INICIO_FICHA'],
                        fecha_terminacion_ficha = row['FECHA_TERMINACION_FICHA'],
                        etapa_ficha=row['ETAPA_FICHA'],
                        modalidad_formacion=row['MODALIDAD_FORMACION'],
                        codigo_sector_programa=row['CODIGO_SECTOR_PROGRAMA'],
                        nombre_sector_programa=row['NOMBRE_SECTOR_PROGRAMA'],
                        codigo_ocupacion=row['CODIGO_OCUPACION'],
                        nombre_ocupacion=row['NOMBRE_OCUPACION'],
                        codigo_programa=row['CODIGO_PROGRAMA'],
                        version_programa=row['VERSION_PROGRAMA'],
                        nombre_programa_formacion=row['NOMBRE_PROGRAMA_FORMACION'],
                        red=row['RED'],
                        codigo_pais_curso=row['CODIGO_PAIS_CURSO'],
                        nombre_pais_curso=row['NOMBRE_PAIS_CURSO'],
                        codigo_departamento_curso=row['CODIGO_DEPARTAMENTO_CURSO'],
                        nombre_departamento_curso=row['NOMBRE_DEPARTAMENTO_CURSO'],
                        codigo_municipio_curso=row['CODIGO_MUNICIPIO_CURSO'],
                        nombre_municipio_curso=row['NOMBRE_MUNICIPIO_CURSO'],
                        codigo_convenio=row['CODIGO_CONVENIO'],
                        nombre_convenio=row['NOMBRE_CONVENIO'],
                        ampliacion_cobertura=row['AMPLIACION_COBERTURA'],
                        codigo_programa_especial=row['CODIGO_PROGRAMA_ESPECIAL'],
                        nombre_programa_especial=row['NOMBRE_PROGRAMA_ESPECIAL'],
                        numero_cursos=row['NUMERO_CURSOS'],
                        total_aprendices_masculinos=row['TOTAL_APRENDICES_MASCULINOS'],
                        total_aprendices_femeninos=row['TOTAL_APRENDICES_FEMENINOS'],
                        total_aprendices_nobinario=row['TOTAL_APRENDICES_NOBINARIO'],
                        total_aprendices=row['TOTAL_APRENDICES'],

                        total_aprendices_activos=row['TOTAL_APRENDICES_ACTIVOS'],
                        duracion_programa=row['DURACION_PROGRAMA'],
                        nombre_nuevo_sector=row['NOMBRE_NUEVO_SECTOR'],
                        per_documento=selected_persona
                     
                    )
                    
                    p.per_documento = selected_persona
                    p.save()

            
                print("Datos guardados exitosamente.")

            except Exception as e:
                print(f"Error al procesar el archivo: {str(e)}")
        
    return redirect('personas:P04')


def Poblacion_vulnerable(request):
    
    per_documento = Persona.objects.all()
    return render( request, 'Poblacion_vulnerable/poblacion_vulnerable.html', {'per_documento':per_documento})
    
def  Subir_poblacion_vulnerable(request):
    
    if request.method == 'POST':
        archivo = request.FILES.get('fileUpload')
        per_documento = request.POST.get('per_documento')
        
        if archivo and archivo.name.endswith('.xlsx'):
            try:
                select_persona = Persona.objects.get(per_documento=per_documento)
                df = pd.read_excel(archivo)
                
                
                columnas = ['Indicadores', 'Meta 2024', 'Ejecución','% de Ejecución']
                indicadores = df['Indicador'].tolist()
                
                for index, row in df.iterrows():
                    inndicador_principal = row['Indicadores']
                    subgrupo1 = row['Indígenas']
                    subgrupo2 = row['Cupos']
                    subgrupo3 = row['Aprendices']
                
            except Exception as e:
                print(f"Error al procesar el archivo: {str(e)}")
                
                
import pandas as pd
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ExcelUploadForm
from .models import Indicador
#excel_file
import pandas as pd
from pyxlsb import open_workbook
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ExcelUploadForm
from .models import Indicador, Persona
from django.utils import timezone
from io import BytesIO

def upload_excel(request):
    if request.method == 'POST':
        per_documento = request.POST.get('per_documento')
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['excel_file']

            if not hasattr(excel_file, 'read'):
                return render(request, 'upload.html', {'form': form, 'error': "El archivo subido no es válido."})

            try:
                # Leer el archivo en un flujo de bytes
                file_stream = BytesIO(excel_file.read())

                # Usar pyxlsb para abrir el archivo .xlsb desde el flujo de bytes
                with open_workbook(file_stream) as wb:
                    # Imprimir los nombres de las hojas para verificar el índice
                    sheet_names = [sheet.name for sheet in wb.sheets]
                    print("Nombres de las hojas:", sheet_names)

                    # Leer la hoja llamada 'RESUMEN'
                    sheet = wb.get_sheet(1)  # La segunda hoja (índice 1)

                    # Leer todas las filas de la hoja
                    data = []
                    for row in sheet.rows():
                        data.append([cell.v for cell in row])

                # Convertir los datos a un DataFrame de pandas
                df = pd.DataFrame(data[1:], columns=data[0])
                print("DataFrame leído del archivo Excel:")
                print(df.head())
                print("Columnas del DataFrame:")
                print(df.columns)

                # Asegúrate de que per_documento existe en Persona
                selected_persona = Persona.objects.get(per_documento=per_documento)

                # Procesar las columnas del DataFrame
                for _, row in df.iterrows():
                    Indicador.objects.create(
                        nombre=row.get('Indicador', ''),
                        pobl_fecha_poblacion=timezone.now(),
                        indigenas_cupos_meta=row.get(('Indígenas', 'Cupos'), 0),
                        indigenas_aprendices_meta=row.get(('Indígenas', 'Aprendices'), 0),
                        inpec_cupos_meta=row.get(('INPEC', 'Cupos'), 0),
                        inpec_aprendices_meta=row.get(('INPEC', 'Aprendices'), 0),
                        jovenes_cupos_meta=row.get(('Jóvenes Vulnerables', 'Cupos'), 0),
                        jovenes_aprendices_meta=row.get(('Jóvenes Vulnerables', 'Aprendices'), 0),
                        adolescente_cupos_meta=row.get(('Adolescente Conflicto', 'Cupos'), 0),
                        adolescente_aprendices_meta=row.get(('Adolescente Conflicto', 'Aprendices'), 0),
                        mujer_cupos_meta=row.get(('Mujer Cabeza de Hogar', 'Cupos'), 0),
                        mujer_aprendices_meta=row.get(('Mujer Cabeza de Hogar', 'Aprendices'), 0),
                        indigenas_cupos_ejecucion=row.get(('Indígenas', 'Cupos Ejecución'), 0),
                        indigenas_aprendices_ejecucion=row.get(('Indígenas', 'Aprendices Ejecución'), 0),
                        inpec_cupos_ejecucion=row.get(('INPEC', 'Cupos Ejecución'), 0),
                        inpec_aprendices_ejecucion=row.get(('INPEC', 'Aprendices Ejecución'), 0),
                        jovenes_cupos_ejecucion=row.get(('Jóvenes Vulnerables', 'Cupos Ejecución'), 0),
                        jovenes_aprendices_ejecucion=row.get(('Jóvenes Vulnerables', 'Aprendices Ejecución'), 0),
                        adolescente_cupos_ejecucion=row.get(('Adolescente Conflicto', 'Cupos Ejecución'), 0),
                        adolescente_aprendices_ejecucion=row.get(('Adolescente Conflicto', 'Aprendices Ejecución'), 0),
                        mujer_cupos_ejecucion=row.get(('Mujer Cabeza de Hogar', 'Cupos Ejecución'), 0),
                        mujer_aprendices_ejecucion=row.get(('Mujer Cabeza de Hogar', 'Aprendices Ejecución'), 0),
                        per_documento=selected_persona
                    )

                return HttpResponseRedirect('/success/')
            except Exception as e:
                print(f"Error al leer el archivo Excel: {e}")
                return render(request, 'Poblacion_vulnerable/poblacion_vulnerable.html', {'form': form, 'error': str(e)})
    else:
        form = ExcelUploadForm()
    return render(request, 'Poblacion_vulnerable/poblacion_vulnerable.html', {'form': form})
