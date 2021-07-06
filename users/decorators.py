from django.shortcuts import redirect
from django.http import HttpResponse


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_company:
            return redirect('company-feed', request.user.id)
        elif request.user.is_authenticated and request.user.is_buyer:
            return redirect('buyer-feed')
        elif request.user.is_authenticated and request.user.is_DeliveryMan:
            return redirect('deliveryMan-feed')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def show_to_buyer(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.is_admin or request.user.is_buyer:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not authorized to view this page")

        return wrapper_func

    return decorator


def show_to_company(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.is_admin or request.user.is_company:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not authorized to view this page")

        return wrapper_func

    return decorator

def show_to_deliveryMan(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.is_admin or request.user.is_DeliveryMan:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not authorized to view this page")

        return wrapper_func

    return decorator
