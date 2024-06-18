from django.shortcuts import render

def menu(request):
    return render(request,'home.html')

def inicio_sesion(request):
    return render(request,'inicio_sesion.html')