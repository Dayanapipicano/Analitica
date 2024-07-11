from django import forms
from apps.core.models import Municipios
class MunicipiosForm(forms.Form):
    model = Municipios
    fields  = ['nombre']
    Widget = {
            'nombre': forms.Select(attrs={'class':'form-control'})
        }