from django import forms
from .models import Persona
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm



class PersonaForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electrónico", max_length=50, help_text="Coloca tu correo electrónico", error_messages={'invalid': 'Solo puedes colocar caracteres válidos para el email'})

    class Meta:
        model = Persona
        fields = ['per_documento', 'per_tipo_documento', 'email', 'per_nombres', 'per_apellidos', 'per_telefono', 'password1', 'password2']
    
    def clean_per_correo(self):
        email = self.cleaned_data.get('email').lower()
        if Persona.objects.filter(email=email).exists():
            raise ValidationError("El correo electrónico ya ha sido tomado")
        return email

    def save(self, commit=True):
        user = super(PersonaForm, self).save(commit=False)
        user.per_correo = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    


class LoginForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)


