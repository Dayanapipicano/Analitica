from apps.personas.models import Meta
from apps.core.models import Centro_de_formacion
from apps.personas.models import Metas_formacion,Modalidad,Estrategia, Estrategia_detalle,Persona
from django.core.exceptions import ValidationError
from django import forms
class Form_meta(forms.ModelForm):
    
    
    met_centro_formacion = forms.ChoiceField(choices=[],widget=forms.Select(attrs={'class':'form-control'}))
    
    class Meta:
        model = Meta
        fields = [
        
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
        'per_documento'
        ]
        
        widgets =  {
            'met_fecha_inicio': forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
            'met_fecha_fin': forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
            
            'met_centro_formacion': forms.TextInput(attrs={'class':'form-control','aria-label':'Centro de formacion','oninput': 'this.value = this.value.replace(/[^0-9]/g, "");'}),
            'met_codigo': forms.TextInput(attrs={'class':'form-control','aria-label':'Centro de formacion'}),
            'met_año': forms.TextInput(attrs={'class':'form-control','aria-label':'Centro de formacion','oninput': 'this.value = this.value.replace(/[^0-9]/g, "");'}),
            'met_total_otras_poblaciones': forms.TextInput(attrs={'class':'form-control','aria-label':'Centro de formacion','oninput': 'this.value = this.value.replace(/[^0-9]/g, "");'}),
            'met_total_victimas': forms.TextInput(attrs={'class':'form-control','aria-label':'Centro de formacion','oninput': 'this.value = this.value.replace(/[^0-9]/g, "");'}),
            'met_total_hechos_victimizantes': forms.TextInput(attrs={'class':'form-control','aria-label':'Centro de formacion','oninput': 'this.value = this.value.replace(/[^0-9]/g, "");'}),
            'met_total_desplazados_violencia': forms.TextInput(attrs={'class':'form-control','aria-label':'Centro de formacion','oninput': 'this.value = this.value.replace(/[^0-9]/g, "");'}),
            'met_total_titulada': forms.TextInput(attrs={'class':'form-control','aria-label':'Centro de formacion','oninput': 'this.value = this.value.replace(/[^0-9]/g, "");'}),
            'met_total_complementaria': forms.TextInput(attrs={'class':'form-control','aria-label':'Centro de formacion','oninput': 'this.value = this.value.replace(/[^0-9]/g, "");'}),
            'met_total_poblacion_vulnerable': forms.TextInput(attrs={'class':'form-control','aria-label':'Centro de formacion','oninput': 'this.value = this.value.replace(/[^0-9]/g, "");'}),
            
           
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['met_centro_formacion'].choices = Centro_de_formacion.Centro_de_formacion_choices.choices
        self.fields['per_documento'].widget =  forms.HiddenInput()
       
    def clean_meta_año(self):
        met_años = self.cleaned_data.get('met_año')
        if Meta.objects.filter(met_año=met_años).exists():
            raise forms.ValidationError('Este año ya existe')
        
       
        if len(str(met_años)) > 4:
            raise ValidationError('El año no puede tener mas de 4 caracteres')
        return met_años
    
class Form_meta_formacion(forms.ModelForm):
    
    
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
    
    

#ESTRATEGIAS INSTITUCINALES


class Form_estrategias(forms.ModelForm):
    
    
    class Meta:
        model = Estrategia
        fields = [
         
            'est_nombre',
            'est_modalidad',
            'met_id',
            'est_total_meta',
            
        ]
        
    
   
        def __init__(self, *args, **kwargs):
       
        #para bloquear el campo y solo visualizar 
           self.fields['est_total_meta'].widget.attrs['readonly'] = True
        
        
        
class Form_meta_estrategia_detalle(forms.ModelForm):
    
    estd_modalidad =forms.ModelChoiceField(queryset=Modalidad.objects.all(),to_field_name='id',widget=forms.Select)
    est_id = forms.ModelChoiceField(queryset=Estrategia.objects.none())
 
    class Meta: 
        model = Estrategia_detalle
        fields = {
            "est_id",
            'estd_modalidad',
            'estd_operario_meta',
            'estd_auxiliar_meta',
            'estd_tecnico_meta',
            'estd_profundizacion_tecnica_meta',
            'estd_tecnologo',
            'estd_evento',
            'estd_curso_especial',
            'estd_bilinguismo',
            'estd_sin_bilinguismo',
            'estd_meta',
        }
        widgets =  {
            'estd_meta': forms.Select(attrs={'class':'form_control'}),
           

        }
        
 
        
class Form_modalidad(forms.ModelForm):
    
    class Meta:
        model = Modalidad
        fields = [
            'modalidad'
        ]
    
        
    
    
