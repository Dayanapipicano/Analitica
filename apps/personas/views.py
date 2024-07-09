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
                return redirect('personas:Home')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos')
        else:
            # Manejo de errores de formulario si no es válido
            errors = formPersona.errors.as_data()
            for field, error_list in errors.items():
                for error in error_list:
                    messages.error(request, f'{field}: {error.message}')

    else:
        formPersona = LoginForm()
    
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

