from apps.personas.models import Meta
from django import forms
class Form_meta(forms.ModelForm):
    
    class Meta:
        model = Meta
        fields = [
        'met_id',
        'met_centro_formacion',
        'met_codigo',
        'met_fecha_inicio',
        'met_fecha_fin',
        'met_año',
        'met_total_otras_poblaciones',
        'met_total_victimas',
        'met_total_hechos_victimizantes',
        'met_total_desplazados_violencia',
        'met_total_titulada',
        'met_total_complementaria',
        'met_total_poblacion_vulnerable',
        'persona',
    ]
   
    
    
