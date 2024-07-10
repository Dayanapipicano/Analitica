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
        print('Datos recibidos en POST:', request.POST)  
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
def Editar_perfil(request,per_documento):
    persona = Persona.objects.get(per_documento=per_documento)
    
    if request.method == 'GET':
        formPersona = EditProfileForm(instance=persona)
        
    else:
        formPersona = EditProfileForm(request.POST, instance=persona)
        if formPersona.is_valid():
            formPersona.save()
        return redirect(reverse('personas:editar_perfil',kwargs={'per_documento': per_documento}))
    return render(request, 'perfil.html',{'formPersona':formPersona})


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

#subir el P04
# views.py

# views.py

# views.py

import pandas as pd
from django.shortcuts import render
from apps.personas.models import P04
import pandas as pd
from django.utils import timezone

import pandas as pd
import numpy as np
from django.utils import timezone
from .models import P04

def subir_archivo(request):
    if request.method == 'POST':
        archivo = request.FILES.get('fileUpload')

        if archivo and archivo.name.endswith('.xlsx'):  # Verifica si es un archivo Excel
            try:
                # Carga el archivo Excel, empezando desde la fila 5 para los nombres de las columnas (header=4)
                df = pd.read_excel(archivo, header=4)

                # Reemplaza los valores vacíos por NaN
                df = df.replace(r'^\s*$', np.nan, regex=True)

                # Imprime las columnas disponibles en el DataFrame para verificar
                print("Columnas disponibles en df:")
                print(df.columns)

                # Itera sobre las filas del DataFrame
                for index, row in df.iterrows():
                    # Verifica si hay datos incompletos en la fila actual y omítela si es necesario
                    if row.isnull().any():
                        print(f"Datos incompletos en la fila {index}. Se omitirá.")
                        continue

                    # Crea una instancia de P04 y asigna los valores de las columnas por nombre
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
                       
                    )
                    # Guarda la instancia P04 en la base de datos
                    p.save()

                # Éxito: archivo procesado correctamente
                print("Datos guardados exitosamente.")

            except Exception as e:
                print(f"Error al procesar el archivo: {str(e)}")
        
    return render(request, 'p04.html')
