from django.contrib.auth.decorators import *
from users.models import *
from .models import *
from django.shortcuts import render
from .forms import *
from .utils import *
from users.decorators import *

@login_required(login_url='login')
@show_to_buyer(allowed_roles=['admin', 'is_buyer'])
def view_cart(request,pk):
    user = User.objects.get(id=pk)
    
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            product_user=request.POST['product_user']
            product_name=request.POST['product_name']
            pro_user=User.objects.get(email=product_user)
            product=ProductModel.objects.get(user=pro_user,name=product_name)
            plus=request.POST.get('plus',False)
            minus=request.POST.get('minus',False)
            delete=request.POST.get('delete',False)
            ordered = OrderModel.objects.get(buyer=request.user, product=product)
            if plus:
                if product.availQuantity>ordered.count:
                    ordered.count=ordered.count+1
                    ordered.total=product.price*ordered.count
                    ordered.save()
            if minus:
                if ordered.count>1:
                    ordered.count=ordered.count-1
                    ordered.total=product.price*ordered.count
                    ordered.save()
            if delete:
                ordered.delete()
    order_list = OrderModel.objects.filter(buyer=user)
    total=0
    for order in order_list:
        total=total+order.total
    
    context = {
            'user': user,
            'order_list': order_list,
            'total':total,
            'form':form,
        }
    return render(request, 'view-cart.html', context)