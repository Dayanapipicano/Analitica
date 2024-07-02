from django.urls import path
from apps.personas import views

app_name = 'personas'

urlpatterns = [
    path('registro/',views.Registro, name='registro')
]
