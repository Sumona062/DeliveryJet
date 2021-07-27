from django import forms
from django.contrib.auth.forms import authenticate
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from users.models import*


class OrderForm(ModelForm):
    class Meta:
        model = OrderModel
        fields = ()