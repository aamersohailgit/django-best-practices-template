from .models import ModelFieldPermission

class FieldPermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        model_name = view_kwargs.get('model_name', None)
        field_name = view_kwargs.get('field_name', None)
        
        if model_name and field_name:
            try:
                permission = ModelFieldPermission.objects.get(user=request.user, model_name=model_name, field_name=field_name)
                if not permission.can_access:
                    # Redirect or raise a Permission Denied error based on your requirements
                    return redirect('permission_denied_view') # This view should be defined to show a "Permission Denied" message
            except ModelFieldPermission.DoesNotExist:
                pass
