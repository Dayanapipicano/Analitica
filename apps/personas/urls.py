from django.urls import path
from apps.personas import views

app_name = 'personas'

urlpatterns = [
    path('registro/',views.Registro, name='registro'),
    path('inicio_sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('home/', views.Home, name='Home'),
]
