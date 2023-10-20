from django.http import HttpResponseForbidden
from .models import ModelFieldPermission

def check_field_permission(model_name, field_name):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            try:
                permission = ModelFieldPermission.objects.get(user=request.user, model_name=model_name, field_name=field_name)
                if not permission.can_access:
                    return HttpResponseForbidden("You don't have permission to access this field.")
            except ModelFieldPermission.DoesNotExist:
                pass
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
