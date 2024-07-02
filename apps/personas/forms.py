from django import forms
from .models import Persona
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

class PersonaForm(forms.ModelForm):
    
    class Meta:
        model = Persona
        fields = ['per_documento', 'per_tipo_documento', 'per_correo','per_nombres','per_apellidos','per_telefono']
        


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electrónico", max_length=50, help_text="Coloca tu correo electrónico", error_messages={'invalid': 'Solo puedes colocar caracteres válidos para el email'})

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if Persona.objects.filter(email=email).exists():
            raise ValidationError("El correo electrónico ya ha sido tomado")
        return email

    def save(self, commit=True):
        user = Persona.objects.create_user(
            self.cleaned_data["username"],
            self.cleaned_data["email"],
            self.cleaned_data["password1"],
        )
        return user
