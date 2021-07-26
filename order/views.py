from django.contrib.auth.decorators import *
from users.models import User
from django.shortcuts import render
from .forms import *
from .utils import *
from users.decorators import *

@login_required(login_url='login')
@show_to_buyer(allowed_roles=['admin', 'is_buyer'])
def view_cart(request,pk):
    user = User.objects.get(id=pk)
    return render(request, 'view-cart.html')

