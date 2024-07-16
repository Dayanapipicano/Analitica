from django.urls import path
from apps.core import views as core_views


app_name = 'cores'
urlpatterns = [
    path('crear_metas_formacion', core_views.Crear_metas_formacion, name='Crear_metas_formacion'),
    path('cobertura/index', core_views.cobertura, name="cobertura"),
    path('cobertura_mapa/', core_views.Cobertura_mapa.as_view(), name='cobertura_mapa'),
    path('modalidad/', core_views.Modalidad, name='modalidad'),
    path('programa/index', core_views.Programa_index, name="programa_index"),
    path('programa/', core_views.Programa.as_view(), name='programa'),
    path('ficha/<int:identificador_ficha>/', core_views.detalle_ficha, name='detalle_ficha'),
    path('desercion/index', core_views.Desercion_index, name="desercion_index"),
    path('desercion', core_views.Desercion.as_view(), name="Desercion"),
]
