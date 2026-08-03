from django.shortcuts import redirect

def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")

        if not request.user.is_superuser:
            return redirect("inicio")  # o mostrar error 403 si quieres

        return view_func(request, *args, **kwargs)
    
    return wrapper
