from django.shortcuts import render
from django.views.generic import CreateView
from apps.personas.models import Persona
from apps.personas.forms import PersonaForm, CustomUserCreationForm
from django.shortcuts import render, redirect

def Registro(request):
    if request.method == 'POST':
        formPersona = PersonaForm(data=request.POST)
        if formPersona.is_valid():
            persona = formPersona.save()
            if persona is not None:
                return redirect('inicio_sesion')
            
    else:
        formPersona = PersonaForm()
    return render(request,'registro.html',{'formPersona': formPersona})