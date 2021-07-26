from django import forms
from django.contrib.auth.forms import authenticate
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from order.models import*


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Email or Password is incorrect")


class BuyerRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text='Required. Add a valid email address')
    name = forms.CharField(max_length=60,help_text='Required.')
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
        help_text='Password must contain at least 8 character including numeric values',
    )
    is_buyer = forms.BooleanField(initial=True)


    class Meta:
        model = User
        fields = ("name", "email", "password1", "password2", "is_buyer")


class CompanyRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text='Required. Add a valid email address')
    name = forms.CharField(max_length=60,help_text='Required.')
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
        help_text='Password must contain at least 8 character including numeric values',
    )
    is_company = forms.BooleanField(initial=True)

    class Meta:
        model = User
        fields = ("name", "email", "password1", "password2", "is_company")


class DeliveryManRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text='Required. Add a valid email address')
    name = forms.CharField(max_length=60,help_text='Required.')
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
        help_text='Password must contain at least 8 character including numeric values',
    )
    is_DeliveryMan = forms.BooleanField(initial=True)

    class Meta:
        model = User
        fields = ("name", "email", "password1", "password2", "is_DeliveryMan")

class CompanyEditProfileForm(ModelForm):
    logo = forms.ImageField(required=False, error_messages={'invalid': "Image files only"}, widget=forms.FileInput)

    class Meta:
        model = CompanyModel
        fields = '__all__'
        exclude = ['user']


class BuyerEditProfileForm(ModelForm):
    image = forms.ImageField(required=False, error_messages={'invalid': "Image files only"}, widget=forms.FileInput)

    class Meta:
        model = BuyerModel
        fields = '__all__'
        exclude = ['user']


class DeliveryManEditProfileForm(ModelForm):
    image = forms.ImageField(required=False, error_messages={'invalid': "Image files only"}, widget=forms.FileInput)

    class Meta:
        model = DeliveryManModel
        fields = '__all__'
        exclude = ['user']


class PostProductForm(ModelForm):
    image = forms.ImageField(required=False, error_messages={'invalid': "Image files only"}, widget=forms.FileInput)

    class Meta:
        model = ProductModel
        fields = '__all__'
        exclude = ['user']




class AccountInformationForm(ModelForm):
    class Meta:
        model = User
        fields = ('name', 'email')


class OrderForm(ModelForm):
    class Meta:
        model = OrderModel
        fields = ()