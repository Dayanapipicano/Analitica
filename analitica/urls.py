"""
URL configuration for analitica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.menu, name="menu"),
    path('inicio_sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('registro/', views.registro, name="registro"),
    
    #COBERTURA
    
    path('cobertura/index', views.cobertura, name="cobertura"),
    path('desercion/index', views.desercion, name="desercion"),
    path('estrategias/index', views.estrategias, name="estrategias"),
    path('estrategias_institucionales/index', views.estrategias_institucionales, name="estrategias_institucionales"),
    path('formacion_regular/index', views.formacion_regular, name="formacion_regular"),
    path('general/index', views.general, name="general"),
    path('poblacion_vulnerable/index', views.poblacion_vulnerable, name="poblacion_vulnerable"),
    path('programa/index', views.programa, name="programa")
]
