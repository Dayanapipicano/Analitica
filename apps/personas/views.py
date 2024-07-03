from django.shortcuts import render
from apps.personas.forms import PersonaForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate


def Home(request):
    return render(request,'home.html')

def Registro(request):
 
   if request.method == 'POST':
        print('Datos recibidos en POST:', request.POST)  # Ver datos enviados
        formPersona = PersonaForm(request.POST)
        if formPersona.is_valid():
            formPersona.save()
            email = formPersona.cleaned_data.get('per_correo')
            raw_password = formPersona.cleaned_data.get('password1')
            user = authenticate(username=email, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('inicio_sesion')
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
        print(formPersona)
        if formPersona.is_valid():
            per_correo = formPersona.cleaned_data['per_correo']
            password = formPersona.cleaned_data['password1']
            user = authenticate(request, per_correo=per_correo, password=password)
          
            if user is not None:
                login(request, user)
                
                return redirect('personas:Home')
            else:
                
               
                formPersona.add_error(None, 'Usuario o contraseña incorrectos')
    else:
        formPersona = LoginForm()
    
    return render(request, 'inicio_sesion.html', {'formPersona': formPersona})
    