from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

def permission_required(permission_codename):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return HttpResponseForbidden("No tienes permiso para acceder a esta vista.")
            
            # Obtener los roles del usuario
            user_roles = request.user.roles.all()
            has_permission = any(
                role.permissions.filter(codename=permission_codename).exists()
                for role in user_roles
            )

            if not has_permission:
                return HttpResponseForbidden("No tienes permiso para acceder a esta vista.")
            
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
