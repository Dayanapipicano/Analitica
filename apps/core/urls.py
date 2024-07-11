from django.urls import path
from apps.core import views as core_views


app_name = 'cores'
urlpatterns = [
    path('crear_metas_formacion', core_views.Crear_metas_formacion, name='Crear_metas_formacion'),
    path('cobertura_mapa/', core_views.Cobertura_mapa.as_view(), name='cobertura_mapa'),
    path('cober/', core_views.cober, name='cober'),
]
