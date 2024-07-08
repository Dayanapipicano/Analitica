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



from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib import messages


class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('personas:perfil')  # Redirige a la URL de perfil después del cambio de contraseña

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, '¡Contraseña cambiada exitosamente!')
        return response

def Home(request):
    return render(request,'home.html')

def Registro(request):
 
   if request.method == 'POST':
        print('Datos recibidos en POST:', request.POST)  # Ver datos enviados
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
                print('Error en autenticación')  # Si la autenticación falla
        else:
            print('Errores en el formulario:', formPersona.errors)  # Mostrar errores de validación
   else:
        formPersona = PersonaForm()
   return render(request,'registro.html',{'formPersona': formPersona})


def inicio_sesion(request):
    if request.method == 'POST':
        formPersona = LoginForm(request.POST)
        if formPersona.is_valid():
            per_documento = formPersona.cleaned_data['per_documento']
            password = formPersona.cleaned_data['password1']
            user = authenticate(request, per_documento=per_documento, password=password)
          
            if user is not None:
                login(request, user)
                return redirect('personas:Home')  # Redirige al 'Home' después de iniciar sesión
            else:
                formPersona.add_error(None, 'Usuario o contraseña incorrectos')
    else:
        formPersona = LoginForm()
    
    return render(request, 'inicio_sesion.html', {'formPersona': formPersona})

def Perfil(request):
    formPersona = EditProfileForm
    return render(request, 'perfil.html',{'formPersona':formPersona})


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

#CAMBIAR LA CONTRASEÑA DE LA PERSONA

