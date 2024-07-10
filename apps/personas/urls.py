from django.urls import path
from apps.personas.views import CustomPasswordChangeView
from apps.personas import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
app_name = 'personas'

urlpatterns = [
    path('registro/',views.Registro, name='registro'),
    path('inicio_sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('home/', views.Home, name='Home'),
    path('perfil/', views.Perfil, name="perfil"),
    path('editar_perfil/<int:per_documento>/', views.Editar_perfil, name="editar_perfil"),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('subir_archivo/', views.subir_archivo, name='subir_archivo'),
    path('P04/', views.p04, name="P04"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
