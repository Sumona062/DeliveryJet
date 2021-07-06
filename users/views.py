from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from users.forms import LoginForm
from users.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash
from django.db.models import Q
from django.shortcuts import render
from django.core.mail import send_mail
from django.utils.html import strip_tags
from .decorators import *
from .decorators import *
from .forms import *
from .utils import *

def home(request):
    buyers = User.objects.filter(is_buyer=True)
    companies = User.objects.filter(is_company=True)
    deliveryMan = User.objects.filter(is_DeliveryMan=True)

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
            BuyerModel.objects.create(user=user)
            return redirect('login')
        else:
            return render(request, 'signup.html', {'formBuyer': formBuyer,"formCompany":formCompany,"formDeliveryMan":formDeliveryMan})


    formBuyer = BuyerRegistrationForm()
    formCompany = CompanyRegistrationForm()
    formDeliveryMan = DeliveryManRegistrationForm()
    context = {
        'buyers': buyers,
        'companies': companies,
        'deliveryMan': deliveryMan,
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
                return redirect('buyer-feed')

            if user and user.is_company :
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                return redirect('company-feed',user.id)

            if user and user.is_DeliveryMan :
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                return redirect('bdeliveryMan-feed')

        else:
            print("bye")
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
def buyer_feed(request):
    

    return render(request, 'buyer/buyer-feed.html')

@login_required(login_url='login')
@show_to_deliveryMan(allowed_roles=['admin', 'is_DeliveryMan'])
def deliveryMan_feed(request):
    

    return render(request, 'deliveryMan/deliveryMan-feed.html')
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

    
    context = {
        'user': user,
        'location_link': location_link,
        
    }
    return render(request, 'company/company-feed.html', context)



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