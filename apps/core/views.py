from django.shortcuts import render
from apps.personas.models import Persona
def menu(request):
    return render(request,'home.html')

def inicio_sesion(request):
    return render(request,'inicio_sesion.html')

def registro(request):
    return render(request, 'registro.html')

def cobertura(request):
    return render(request, 'Cobertura/cobertura.html')


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

def programa(request):
    return render(request, 'Programa/programa.html')




def recuperar_contraseña(request):
    return render(request, 'recuperar_contraseña.html')
def grafica(request):
    return render(request, 'Estrategias/grafica.html')




def administrador(request):
    return render(request, 'administrador.html')