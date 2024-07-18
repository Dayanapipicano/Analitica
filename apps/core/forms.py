from apps.personas.models import Meta
from apps.core.models import Centro_de_formacion
from apps.personas.models import Metas_formacion,Modalidad

from django import forms
class Form_meta(forms.ModelForm):
    
    
    met_centro_formacion = forms.ChoiceField(choices=[],widget=forms.Select(attrs={'class':'form-control'}))
    
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
        'per_documento',
        ]
        
        widgets =  {
            'met_fecha_inicio': forms.DateInput(attrs={'class':'form_control', 'type': 'date'}),
            'met_fecha_fin': forms.DateInput(attrs={'class':'form_control', 'type': 'date'}),
           
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['met_centro_formacion'].choices = Centro_de_formacion.Centro_de_formacion_choices.choices

    
class Form_meta_formacion(forms.ModelForm):
    
    metd_modalidad = forms.ChoiceField(choices=[], widget=forms.Select(attrs={'class':'form-control'}))
    
    class Meta:
        model = Metas_formacion
        fields = [
            'metd_id',
            'metd_modalidad',
            'met_formacion_operario',
            'met_formacion_auxiliar',
            'met_formacion_tecnico',
            'met_formacion_profundizacion_tecnica',
            'met_formacion_tecnologo',
            'met_formacion_evento',
            'met_formacion_curso_especial',
            'met_formacion_bilinguismo',
            'met_formacion_sin_bilinguismo',
            'met_id',
            
            
        ]
    
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['metd_modalidad'].choices = Modalidad.Modalidad_choices.choices

