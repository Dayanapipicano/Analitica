from django.urls import path
from apps.core import views as core_views


app_name = 'cores'
urlpatterns = [
 
    path('cobertura/index', core_views.cobertura, name="cobertura"),
    path('cobertura_mapa/', core_views.Cobertura_mapa.as_view(), name='cobertura_mapa'),
    path('modalidad/index/', core_views.Modalidad, name='modalidad'),
    path('programa/index', core_views.Programa_index, name="programa_index"),
    path('programa/', core_views.Programa.as_view(), name='programa'),
    path('ficha/<int:identificador_ficha>/', core_views.detalle_ficha, name='detalle_ficha'),
    path('desercion/index', core_views.Desercion_index, name="desercion_index"),
    path('desercion', core_views.Desercion.as_view(), name="Desercion"),
    path('formacion_regular/index', core_views.Formacion_regular_index, name='formacion_regular_index'),
    path('metas/create/', core_views.Meta_create.as_view(), name="meta_create"),
    path('metas_formacion/create/', core_views.Meta_formacion_create.as_view(), name="meta_formacion_create"),
    path('estrategias_institucionales/index/', core_views.Estrategias_institucionales_index, name='estrategias_institucionales_index'),
    path('estrategias/create/', core_views.Estrategias_create.as_view(), name='estrategias_create'),
    path('estrategias/est_total_meta/<int:met_id>/', core_views.get_meta_valores, name='est_total_meta'),
    path('meta_estrategia_detalle/create', core_views.Meta_estrategia_detalle.as_view(), name="meta_estrategia_detalle"),

]   
