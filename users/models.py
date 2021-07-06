from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from ckeditor.fields import RichTextField


class MyUserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Must have an email address')

        if not name:
            raise ValueError('Must have a name')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, name, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email=self.normalize_email(email),
            name=name,
            password=password,
        )
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_buyer = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
    is_DeliveryMan = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']  # Email & Password are required by default.

    objects = MyUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class BuyerModel(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES, null=True, blank=True)

class DeliveryManModel(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    bio =  models.CharField(max_length=255, choices=GENDER_CHOICES, null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)

class CompanyModel(models.Model):
    TYPE_CHOICES=[
        ('Drug store','Drug store'),
        ('Home Appliances Store' ,'Home Appliances Store'),
        ('Electronic Store','Electronic Store'),
        ('Food marts','Food marts'),
        ('Fashion house','Fashion house'),
        ('Sports hub','Sports hub'),
        ('Lifestyle store','Lifestyle store'),
        ('Mom and kids','Mom and kids'),
        ('Cosmetics House','Cosmetics House'),
        ('book store','book store')
    ]
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    about = RichTextField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    logo = models.ImageField(null=True,blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    type=models.CharField(max_length=255, choices=TYPE_CHOICES, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)

 

class TimeSlotModel(models.Model):
    Time_choices = [
        ('9am-12pm', '9am-12pm'),
        ('12pm-3pm', '12pm-3pm'),
        ('3pm-6pm', '3pm-6pm'),
        ('6pm-9pm', '6pm-9pm'),
    ]
    Day_choices = [
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),

    ]
    time=models.CharField(max_length=255, choices=Time_choices, null=True, blank=True)
    Day = models.CharField(max_length=255, choices=Day_choices, null=True, blank=True)

class AddressPhoneModel(models.Model):
    user=models.ForeignKey(User, null=True,on_delete=models.CASCADE)
    division=models.CharField(max_length=100, null=True, blank=True)
    district=models.CharField(max_length=100, null=True, blank=True)
    thana=models.CharField(max_length=100, null=True, blank=True)
    areaName=models.CharField(max_length=100, null=True, blank=True)
    holdingNo=models.CharField(max_length=100, null=True, blank=True)
    postOffice=models.CharField(max_length=100, null=True, blank=True)
    additonal=models.CharField(max_length=1000, null=True, blank=True)
    phone=models.CharField(max_length=255, null=True, blank=True)


class AvailabilityModel(models.Model):
    address = models.ForeignKey(AddressPhoneModel, null=True, on_delete=models.SET_NULL)
    slot_id=models.ForeignKey(TimeSlotModel, null=True,on_delete=models.SET_NULL)

class PreferredAreaModel(models.Model):
    user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    area=models.CharField(max_length=255, null=True, blank=True)

class ProductModel(models.Model):
    user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=255, null=True, blank=True)
    price=models.CharField(max_length=255, null=True, blank=True)
    category=models.CharField(max_length=255, null=True, blank=True)
    image=models.ImageField(null=True,blank=True)
    refill=models.CharField(max_length=255, null=True, blank=True)
