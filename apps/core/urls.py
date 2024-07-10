from django.urls import path
from apps.core import views as core_views


app_name = 'cores'
urlpatterns = [
    path('crear_metas_formacion', core_views.Crear_metas_formacion, name='Crear_metas_formacion'),
]
