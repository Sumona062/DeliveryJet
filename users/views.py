from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from users.forms import LoginForm
from users.models import User
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login, logout, update_session_auth_hash
from django.db.models import Q
from django.shortcuts import render
from django.core.mail import send_mail
from django.utils.html import strip_tags
from users.decorators import *
from .forms import *
from .utils import *

@unauthenticated_user
def home(request):
    if request.method == 'POST':
        formBuyer = BuyerRegistrationForm(request.POST)
        formCompany= CompanyRegistrationForm(request.POST)
        formDeliveryMan = DeliveryManRegistrationForm(request.POST)
        if formBuyer.is_valid():
            formBuyer.save()
            email = formBuyer.cleaned_data.get('email')
            raw_password = formBuyer.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            BuyerModel.objects.create(user=user)
            print(email,raw_password)
            return redirect('login')

        elif formCompany.is_valid():
            formCompany.save()
            email = formCompany.cleaned_data.get('email')
            raw_password = formCompany.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            CompanyModel.objects.create(user=user)
            return redirect('login')


        elif formDeliveryMan.is_valid():
            formDeliveryMan.save()
            email = formDeliveryMan.cleaned_data.get('email')
            raw_password = formDeliveryMan.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            DeliveryManModel.objects.create(user=user)
            return redirect('login')
        else:
            return render(request, 'signup.html', {'formBuyer': formBuyer,"formCompany":formCompany,"formDeliveryMan":formDeliveryMan})


    formBuyer = BuyerRegistrationForm()
    formCompany = CompanyRegistrationForm()
    formDeliveryMan = DeliveryManRegistrationForm()
    context = {
        "formBuyer": formBuyer,
        "formCompany":formCompany,
        "formDeliveryMan":formDeliveryMan
    }
    
    return render(request, 'signup.html', context)


@unauthenticated_user
def login_page(request):
    if request.POST:
        form = LoginForm(request.POST)
       
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user and user.is_buyer :
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                return redirect('buyer-feed',user.id)

            if user and user.is_company :
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                return redirect('company-feed',user.id)

            if user and user.is_DeliveryMan :
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                return redirect('deliveryMan-feed',user.id)

        else:
            return render(request, 'login.html', {'form': form})
    form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')



@login_required(login_url='login')
@show_to_buyer(allowed_roles=['admin', 'is_buyer'])
def buyer_feed(request, pk):
    user = User.objects.get(id=pk)
    companies = User.objects.filter(is_company=True)
    type=uniqueCompanyType(companies)
    availability=AvailabilityModel.objects.filter(buyer=request.user)
   
    context = {
        'user': user,
        'companies':companies,
        'type':type,
        'availability':availability,

        
    }
    return render(request, 'buyer/buyer-feed.html', context)

@login_required(login_url='login')
@show_to_deliveryMan(allowed_roles=['admin', 'is_DeliveryMan'])
def deliveryMan_feed(request,pk):
    user = User.objects.get(id=pk)
    preferredArea=PreferredAreaModel.objects.filter(user=request.user)
    for pref in preferredArea:
        print(pref.time,pref.user,pref.area)
    
    context = {
        'user': user,
        'preferredArea':preferredArea,
    }

    return render(request, 'deliveryMan/deliveryMan-feed.html',context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email_add = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(
            subject + " from " + fname + " " + lname + " " + email_add,
            message,
            email_add,
            ['officialjobland777@gmail.com', ],
            # the mail address that the email will be sent to
        )
        messages.success(request, "Feedback sent successfully.")

        return render(request, 'user/contact.html', {})

    return render(request, 'user/contact.html', {})


@login_required(login_url='login')
def company_feed(request, pk):
    user = User.objects.get(id=pk)

    location_link = None

    if user.companymodel.location:
        locations = user.companymodel.location.split(' ')
        location_link = "https://maps.google.com/maps?width=100%25&amp;height=450&amp;hl=en&amp;q="

        for location in locations:
            location_link += location + "%20"

        location_link += "&amp;t=&amp;z=14&amp;ie=UTF8&amp;iwloc=B&amp;output=embed"

    
    
    product_list = ProductModel.objects.filter(user=user)
    product_category=uniqueCategory(product_list)

    order_form = OrderForm()
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            product_name=request.POST['product_name']
            product=ProductModel.objects.get(user=user,name=product_name)
            try:
                ordered = OrderModel.objects.get(buyer=request.user, product=product)
            except:
                ordered = None
            if ordered is not None:
                ordered.count=ordered.count+1
                ordered.total=product.price*ordered.count
                ordered.save()
            else:

                order.buyer = request.user
                order.product=product
                order.count=1
                order.total=product.price
                order.save()

            return redirect('company-feed',user.id)


    context = {
        'user': user,
        'location_link': location_link,
        'product_list': product_list,
        'product_category':product_category,
        'order_form':order_form,
    }
    return render(request, 'company/company-feed.html', context)


@login_required(login_url='login')
def company_feed_category(request, pk, cat):
    user = User.objects.get(id=pk)

    location_link = None

    if user.companymodel.location:
        locations = user.companymodel.location.split(' ')
        location_link = "https://maps.google.com/maps?width=100%25&amp;height=450&amp;hl=en&amp;q="

        for location in locations:
            location_link += location + "%20"

        location_link += "&amp;t=&amp;z=14&amp;ie=UTF8&amp;iwloc=B&amp;output=embed"

    product_list = ProductModel.objects.filter(user=user)
    

    order_form = OrderForm()
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            product_name=request.POST['product_name']
            product=ProductModel.objects.get(user=user,name=product_name)
            try:
                ordered = OrderModel.objects.get(buyer=request.user, product=product)
            except:
                ordered = None
            if ordered is not None:
                ordered.count=ordered.count+1
                ordered.total=product.price*ordered.count
                ordered.save()
            else:

                order.buyer = request.user
                order.product=product
                order.count=1
                order.total=product.price
                order.save()

            return redirect('company-feed-category',user.id,cat)
    
    context = {
        'user': user,
        'location_link': location_link,
        'product_list': product_list,
        'product_category':cat,
    }
    return render(request, 'company/company-feed-category.html', context)

@login_required(login_url='login')
@show_to_company(allowed_roles=['admin', 'is_company'])
def company_edit_profile(request):
    company = request.user.companymodel
    form = CompanyEditProfileForm(instance=company)
    if request.method == 'POST':
        form = CompanyEditProfileForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company-feed', request.user.id)
        else:
            messages.error(request, 'There are a few problems')
            return redirect('company-edit-profile')

    context = {
        'form': form,
    }
    return render(request, 'company/company-edit-profile.html', context)

    
@login_required(login_url='login')
@show_to_deliveryMan(allowed_roles=['admin', 'is_DeliveryMan'])
def deliveryMan_edit_profile(request):
    deliveryMan = request.user.deliverymanmodel
    form = DeliveryManEditProfileForm(instance=deliveryMan)
    prefAreaform=PreferredAreaForm()
    if request.method == 'POST':
        form = DeliveryManEditProfileForm(request.POST, request.FILES, instance=deliveryMan)
        prefAreaform=PreferredAreaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('deliveryMan-feed', request.user.id)

        if prefAreaform.is_valid():
            prefArea=prefAreaform.save(commit=False)
            prefArea.user=request.user
            print(prefArea.user,prefArea.area)
            prefAreaform.save()
            return redirect('deliveryMan-feed', request.user.id)
        else:
            messages.error(request, 'There are a few problems')
            return redirect('deliveryMan-edit-profile')

    context = {
        'form': form,
        'prefAreaform':prefAreaform
    }
    return render(request, 'deliveryMan/deliveryMan-edit-profile.html', context)


@login_required(login_url='login')
@show_to_deliveryMan(allowed_roles=['admin', 'is_DeliveryMan'])
def delete_preferredArea(request,pk):
    PreferredArea=PreferredAreaModel.objects.get(id=pk)
    PreferredArea.delete()

    return redirect('deliveryMan-feed', request.user.id)

@login_required(login_url='login')
@show_to_buyer(allowed_roles=['admin', 'is_buyer'])
def buyer_edit_profile(request):
    buyer = request.user.buyermodel
    form = BuyerEditProfileForm(instance=buyer)
           
    if request.method == 'POST':
        form = BuyerEditProfileForm(request.POST, request.FILES, instance=buyer)
        
        if form.is_valid():
            form.save()
            return redirect('buyer-feed', request.user.id)
        else:
            messages.error(request, 'There are a few problems')
            return redirect('buyer-edit-profile')

    context = {
        'form': form,
    }
    return render(request, 'buyer/buyer-edit-profile.html', context)


@login_required(login_url='login')
@show_to_buyer(allowed_roles=['admin', 'is_buyer'])
def add_availability(request):
    form=AvailabilityForm()
    if request.method == 'POST':
        form=AvailabilityForm(request.POST, request.FILES)
        if form.is_valid():
            availability=form.save(commit=False)
            availability.buyer=request.user
            print(availability.buyer,availability.time,availability.Days,availability.address)
            form.save()
            return redirect('buyer-feed', request.user.id)
        else:
            messages.error(request, 'There are a few problems')
            return redirect('add-availability')

    context = {
        'form':form,
    }
    return render(request, 'buyer/add-availability.html', context)

@login_required(login_url='login')
@show_to_buyer(allowed_roles=['admin', 'is_buyer'])
def delete_availability(request,pk):
    availability=AvailabilityModel.objects.get(id=pk)
    print(availability.buyer,availability.address)
    availability.delete()
   
    
    return redirect('buyer-feed', request.user.id)
 
@login_required(login_url='login')
@show_to_company(allowed_roles=['admin', 'is_company'])
def post_product(request):
    task = "Add"
    form = PostProductForm()

    if request.method == 'POST':
        form = PostProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            form.save()
            return redirect('company-feed', request.user.id)
        else:
            return redirect('post-product')

    context = {
        'task': task,
        'form': form
    }
    return render(request, 'product/post-product.html', context)


@login_required(login_url='login')
@show_to_company(allowed_roles=['admin', 'is_company'])
def edit_product(request, pk):
    task = "Edit"
    product = ProductModel.objects.get(id=pk)
    form = PostProductForm(instance=product)
    if request.method == 'POST':
        form = PostProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('company-feed', request.user.id)
        else:
            return redirect('edit-product', request.ProductModel.id)

    context = {
        'task': task,
        'form': form,
    }
    return render(request, 'product/post-product.html', context)





@login_required(login_url='login')
def account_settings(request, pk):
    user = User.objects.get(id=pk)
    information_form = AccountInformationForm(instance=user)
    password_form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        information_form = AccountInformationForm(request.POST, instance=user)
        password_form = PasswordChangeForm(request.user, request.POST)

        if information_form.is_valid():
            information_form.save()
            if request.user.is_buyer:
                return redirect('buyer-feed',request.user.id)
            elif request.user.is_DeliveryMan:
                return redirect('deliveryMan-feed', request.user.id)
            else:
                return redirect('company-feed', request.user.id)

        elif password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # Important!
            if request.user.is_buyer:
                return redirect('buyer-feed',request.user.id)
            elif request.user.is_DeliveryMan:
                return redirect('deliveryMan-feed', request.user.id)
            else:
                return redirect('company-feed', request.user.id)
        else:
            context = {
                'information_form': information_form,
                'password_form': password_form,
            }
            return render(request, 'account-settings.html', context)

    context = {
        'information_form': information_form,
        'password_form': password_form,
    }
    return render(request, 'account-settings.html', context)
