from django.urls import path
from apps.core import views as core_views


app_name = 'cores'
urlpatterns = [
 
    path('cobertura/index', core_views.cobertura, name="cobertura"),
    path('cobertura_mapa/', core_views.Cobertura_mapa.as_view(), name='cobertura_mapa'),
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
    path('get_estrategia_data/<int:id_estd_modalidad>/', core_views.get_estrategia_data, name='get_estrategia_data'),
    path('meta_data/<int:id_estrategia>/', core_views.meta_data, name='meta_data'),
    path('meta_detalle/<int:estd_meta>/', core_views.meta_detalle, name='meta_detalle'),
    path('filtrar_datos_y_modalidades/',core_views.metas_formacion_filtros.as_view(), name='filtrar_datos_y_modalidades'),
    path('filtrar_estrategias_institucionales/',core_views.estrategias_institucionales_filtros.as_view(), name='filtrar_estrategias_institucionales'),
    
    #MODALIDAD
    path('modalidad/index/', core_views.Modalidad_index, name='modalidad_index'),
    path('modalidad/create/', core_views.Modalidad_create.as_view(), name='modalidad_create'),
    path('modalidad/delete/<int:pk>', core_views.Modalidad_delete.as_view(), name='modalidad_delete'),
    path('modalidad/edit/<int:pk>', core_views.Modalidad_edit.as_view(), name='modalidad_edit'),
    
    #ROLES
    path('asignacion_roles/', core_views.Asignacion_roles, name="asignacion_roles" ),
    
    #GRAFICAS GENERAL
    path('general/index', core_views.general, name="general"),
    
    #estrategias institucionales graficas 
    path('estrategias/index', core_views.estrategias, name="estrategias_index"),
    #ALERTAS
    path('verificar-año/', core_views.Verificar_año, name='verificar_año'),
    #verificaciones de formularios meta formacion 
    path('verificacion_meta_formacion_regular/', core_views.Verificacion_meta_formacion_regular, name="verificacion_meta_formacion_regular")
]   

