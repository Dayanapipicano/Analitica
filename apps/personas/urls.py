from django.urls import path
from apps.personas import views

app_name = 'personas'

urlpatterns = [
    path('registro/',views.Registro, name='registro'),
    path('inicio_sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('home/', views.Home, name='Home'),
    path('perfil/', views.Perfil, name="perfil"),
    path('editar_perfil/<int:per_documento>/', views.Editar_perfil, name="editar_perfil")
]
