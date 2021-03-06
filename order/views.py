from django.contrib.auth.decorators import *
from users.models import *
from .models import *
from users.models import *
from django.shortcuts import render
from .forms import *
from .utils import *
from users.decorators import *
from datetime import date
from datetime import datetime
from django.contrib import messages

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
            now = datetime.now()
            currentTime=now.strftime("%d/%m/%Y %H:%M:%S")
            print(currentTime)
            for order in orderList:
                if order.status=="not checkout":
                    if(selectDeliveryMan(order) is not None):
                        delMan=selectDeliveryMan(order)
                        code=''
                        if OrderScheduleModel.objects.filter().exists():
                            schedules=OrderScheduleModel.objects.filter()
                            for s in schedules:
                                if s.order.product.user==order.product.user and s.postDate == currentTime:
                                    code=s.code
                                    print(s.code)
                                else:
                                    code=randomCode()
                        else:
                            code=randomCode()
                    

                    
                        orderSchedule=OrderScheduleModel(order=order,code=code,postDate=currentTime,deliveryMan=delMan)
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
    
    total=0
    for order in orderlist:
        if order.status=='not checkout':
            total=total+order.total
            order_list.append(order)
    
    orderCount=len(order_list) 
    
    context = {
            'user': user,
            'order_list': order_list,
            'total':total,
            'form':form,
            'orderCount':orderCount
        }
    return render(request, 'view-cart.html', context)



@login_required(login_url='login')
@show_to_buyer(allowed_roles=['admin', 'is_buyer'])
def view_pending(request,pk):
    user = User.objects.get(id=pk)
    orderlist = OrderModel.objects.filter(buyer=user)
    orderPendingList=[]

    for order in orderlist:
        if OrderScheduleModel.objects.filter(order=order).exists():
            schedule=OrderScheduleModel.objects.filter(order=order)
            for s in schedule:
                orderPendingList.append(s)
    pendingCount=len(orderPendingList)
    context = {
            'user': user,
            'orderPendingList':orderPendingList,
            'pendingCount':pendingCount,
        }
    return render(request, 'view-pending.html', context)


@login_required(login_url='login')
def order_details(request,pk):
    order=OrderScheduleModel.objects.get(id=pk)
    deliveryMan=User.objects.get(id=order.deliveryMan.id)
    location_link = None
    

    if order.order.product.user.companymodel.location:
        location_link="https://www.google.com/maps/embed/v1/directions?key=AIzaSyCjkI-TzN9giph0DnS1fFF1liDo9HbyQU0&origin="
        originLocation=minDistanceArea(deliveryMan,order.order.product.user.companymodel.location)
        origin=originLocation.split(' ')
        destination = order.order.product.user.companymodel.location.split(' ')
        for orgn in origin:
            location_link +=orgn+"+"

        location_link += "&destination="

        for des in destination:
            location_link += des+"+"

        location_link += "&avoid=tolls|highways"

    

    #print(location_link)
    availabilityList=AvailabilityModel.objects.filter(buyer=order.order.buyer)

    if request.GET.get('Not Collected'):
        order.is_marked = False
        order.save()
        return redirect('order-details', order.id)

    if request.GET.get('Collected'):
        order.is_marked = True
        order.save()
        return redirect('order-details', order.id)

   

    context = {
        'order':order,
        'location_link':location_link,
        'availabilityList':availabilityList


    }
    return render(request, 'order-details.html', context)



@login_required(login_url='login')
def order_delivered(request,pk):
    order=OrderScheduleModel.objects.get(id=pk)

    message= " "
    
    
    if request.GET.get('code'):
        print("get")
        code = request.GET['code']
        if order.code == code:
            order.order.delete()
            order.delete()
            messages.success(request,"Succesfully delivered the order.")
            return redirect('deliveryMan-feed', request.user.id)
        else:
            message="Order Code does not matched, Please try with the correct Code."
            context = {
                'message':message,
            }

            return render(request, 'delivered.html', context)

    context = {
        'message':message,
    }
    return render(request, 'delivered.html', context)



@login_required(login_url='login')
@show_to_company(allowed_roles=['admin', 'is_company'])
def view_order(request,pk):
    user = User.objects.get(id=pk)

       
    
    orders = OrderScheduleModel.objects.filter()
    orderList=[]
    for o in orders:
        if(o.order.product.user==user):
            orderList.append(o)


    pendingCount=len(orderList)  
    
    context = {
            'user': user,
            'orderList': orderList,
            'pendingCount':pendingCount,
        }
    return render(request, 'view-order.html', context)



