from django.contrib.auth.decorators import *
from users.models import *
from .models import *
from users.models import *
from django.shortcuts import render
from .forms import *
from .utils import *
from users.decorators import *
from datetime import date

@login_required(login_url='login')
@show_to_buyer(allowed_roles=['admin', 'is_buyer'])
def view_cart(request,pk):
    user = User.objects.get(id=pk)
    
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        checkout=request.POST.get('checkout',False)
        if checkout:
            orderList=OrderModel.objects.filter(buyer=user)
            for order in orderList:
                if order.status=="not checkout":
                    
                    delMan=selectDeliveryMan(order)
                    code=randomCode()
                    
                    orderSchedule=OrderScheduleModel(order=order,code=code,postDate=date.today(),deliveryMan=delMan)
                    #print(orderSchedule.order,orderSchedule.deliveryMan)
                    orderSchedule.save()
                    order.status=randomCode()
                    order.save()
                    product_user=order.product.user
                    product_name=order.product.name
                    product=ProductModel.objects.get(user=product_user,name=product_name)
                    product.availQuantity=product.availQuantity-order.count
                    product.save()

        elif form.is_valid():
            product_user=request.POST['product_user']
            product_name=request.POST['product_name']
            pro_user=User.objects.get(email=product_user)
            product=ProductModel.objects.get(user=pro_user,name=product_name)
            plus=request.POST.get('plus',False)
            minus=request.POST.get('minus',False)
            delete=request.POST.get('delete',False)
            
            ordered = OrderModel.objects.get(buyer=request.user, product=product,status='not checkout')
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

        

       
    
    orderlist = OrderModel.objects.filter(buyer=user)
    order_list=[]
    
    orderPendingList=[]
    
    
    total=0
    for order in orderlist:
        if order.status=='not checkout':
            total=total+order.total
            order_list.append(order)

        if OrderScheduleModel.objects.filter(order=order).exists():
            schedule=OrderScheduleModel.objects.filter(order=order)
            for s in schedule:
                orderPendingList.append(s)

    
        
    
    context = {
            'user': user,
            'order_list': order_list,
            'total':total,
            'form':form,
            'orderPendingList':orderPendingList
        }
    return render(request, 'view-cart.html', context)
