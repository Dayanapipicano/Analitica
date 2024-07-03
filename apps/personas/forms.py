from django import forms
from .models import Persona
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

class PersonaForm(UserCreationForm):
    per_correo = forms.EmailField(required=True, label="Correo electrónico", max_length=50, help_text="Coloca tu correo electrónico", error_messages={'invalid': 'Solo puedes colocar caracteres válidos para el email'})

    class Meta:
        model = Persona
        fields = ['per_documento', 'per_tipo_documento', 'per_correo', 'per_nombres', 'per_apellidos', 'per_telefono', 'password1', 'password2']
    
    def clean_per_correo(self):
        per_correo = self.cleaned_data.get('per_correo').lower()
        if Persona.objects.filter(per_correo=per_correo).exists():
            raise ValidationError("El correo electrónico ya ha sido tomado")
        return per_correo

    def save(self, commit=True):
        user = super(PersonaForm, self).save(commit=False)
        user.per_correo = self.cleaned_data['per_correo']
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    


class LoginForm(forms.Form):
    per_correo = forms.EmailField(label='Correo electrónico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
