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
    


import pyxlsb
from django.contrib.auth.models import User
from django.http import HttpResponse
from datetime import datetime
from apps.personas.models import Datos_vulnerables






import pandas as pd
from django.utils import timezone

import pandas as pd
from django.utils import timezone
from django.http import HttpResponse
from .models import Datos

def cargar_datos_desde_xlsb(request):
    if request.method == 'POST':
        excel_file = request.FILES.get('excel_file')
        usuario_id = request.POST.get('per_documento')

        # Leer el archivo Excel
        try:
            df = pd.read_excel(excel_file, sheet_name='RESUMEN', header=None)
            print("Hoja 'RESUMEN' leída correctamente.")
        except ValueError as e:
            print(f"Error al leer la hoja: {e}")
            return HttpResponse("Error al leer la hoja 'RESUMEN'.", status=400)

        # Imprimir las primeras filas para verificar la estructura
        print("Primeras filas del DataFrame:")
        print(df.head(25))

        # Ajustar el DataFrame para usar la fila 18 (índice 17) como encabezado
        df.columns = df.iloc[17]
        df = df.drop(index=range(0, 18)).reset_index(drop=True)

        # Imprimir las primeras filas después de configurar encabezados
        print("Primeras filas del DataFrame después de configurar encabezados:")
        print(df.head(25))

        # Encontrar columnas que contienen 'Cupos' y 'Aprendices'
        cupos_cols = [i for i, header in enumerate(df.columns) if pd.notna(header) and 'Cupos' in str(header)]
        aprendices_cols = [i for i, header in enumerate(df.columns) if pd.notna(header) and 'Aprendices' in str(header)]

        print(f"Columnas 'Cupos': {cupos_cols}")
        print(f"Columnas 'Aprendices': {aprendices_cols}")

        if not cupos_cols or not aprendices_cols:
            return HttpResponse("No se encontraron columnas 'Cupos' o 'Aprendices'.", status=400)

        # Extraer información
        indicadores = ['Meta 2024', 'Ejecución', '% de Ejecución']

        # Asignar nombres de grupos en el orden en que aparecen
        grupos = []
        for idx in range(len(cupos_cols)):
            grupo = df.iloc[0, cupos_cols[idx]]
            grupos.append(grupo)
        
        print(f"Grupos asignados: {grupos}")

        # Extraer datos y guardar en la base de datos
        for idx, grupo in enumerate(grupos):
            for indicador in indicadores:
                try:
                    # Filtrar las filas correspondientes a cada indicador
                    indicator_rows = df[df.iloc[:, 1] == indicador]
                    if indicator_rows.empty:
                        print(f"No se encontraron filas para el grupo '{grupo}' y el indicador '{indicador}'.")
                        continue

                    # Extraer los datos para 'Cupos' y 'Aprendices'
                    cupos_col = cupos_cols[idx]
                    aprendices_col = aprendices_cols[idx]

                    for _, row in indicator_rows.iterrows():
                        if pd.notna(row[cupos_col]):
                            datos_modelo = Datos(
                                indicador=indicador,
                                grupo=grupo,
                                cupos=row[cupos_col],
                                aprendices=None,
                                tipo_dato='Cupos',
                                fecha_subida=timezone.now(),
                                usuario_id=usuario_id
                            )
                            datos_modelo.save()
                            print(f"Datos guardados para {indicador} - {grupo} - Cupos: {row[cupos_col]}.")

                        if pd.notna(row[aprendices_col]):
                            datos_modelo = Datos(
                                indicador=indicador,
                                grupo=grupo,
                                cupos=None,
                                aprendices=row[aprendices_col],
                                tipo_dato='Aprendices',
                                fecha_subida=timezone.now(),
                                usuario_id=usuario_id
                            )
                            datos_modelo.save()
                            print(f"Datos guardados para {indicador} - {grupo} - Aprendices: {row[aprendices_col]}.")

                except KeyError:
                    print(f"No se encontraron datos para {indicador} - {grupo}.")
                except Exception as e:
                    print(f"Error al guardar datos para {indicador} - {grupo}: {e}")

        return HttpResponse("Datos cargados exitosamente.")
    return HttpResponse("Método no permitido.", status=405)



