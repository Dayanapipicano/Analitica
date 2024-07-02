from django.contrib.auth.models import BaseUserManager

class UsuarioManage(BaseUserManager):
    
    def create_user(self, correo, password=None, **kwargs):
        if not correo:
            raise ValueError('El correo es obligatotio')
        
        correo = self.normalize_email(correo)
        personas = self.model(correo=correo, **kwargs)
        
        if password:
            personas.set_password(password)
            
        else:
            raise('La contraseña es obligatoria')
        
        personas.save(using=self._db)
        
        return personas
    
    def create_superuser(self, correo, password=None, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        
        if kwargs.get('is_staff') is not True:
            raise ValueError('Is_staff must have is_staff=true')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Is_staff must have is_superuser=true')
        
        return self.create_user(correo,password, **kwargs)
    