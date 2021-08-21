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

    def getBuyer(self):
        return self.user

class DeliveryManModel(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    TYPE_CHOICES=[
        ('Driving License','Driving License'),
        ('NID','NID'),
        ('Passport','Passport')
    ]


    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    bio =  models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    documentID=models.CharField(max_length=255,  null=False, blank=False,default="")
    documentType=models.CharField(max_length=255, choices=TYPE_CHOICES, null=False, blank=False,default="")

    def getDeliveryMan(self):
        return self.user

class CompanyModel(models.Model):
    TYPE_CHOICES=[
        ('Book Store','Book Store'),
        ('Cosmetics House','Cosmetics House'),
        ('Drug Store','Drug Store'),
        ('Electronic Store','Electronic Store'),
        ('Food Marts','Food Marts'),
        ('Fashion House','Fashion House'),
        ('Home Appliances Store' ,'Home Appliances Store'),
        ('Lifestyle Store','Lifestyle Store'),
        ('Mom and Kids','Mom and Kids'),
        ('Sports Hub','Sports Hub') 
       
    ]
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    about = RichTextField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    logo = models.ImageField(null=True,blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    type=models.CharField(max_length=255, choices=TYPE_CHOICES, null=False, blank=False, default="")
    phone = models.CharField(max_length=255, null=True, blank=True)

    def getCompany(self):
        return self.user

 

class AvailabilityModel(models.Model):
    Time_choices = [
        ('9am-3pm','9am-3pm'),
        ('3pm-9pm', '3pm-9pm'),
    ]
    buyer=models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=1000, null=False, blank=False,default="")
    phone=models.CharField(max_length=255, null=False, blank=False,default="")
    time=models.CharField(max_length=255, choices=Time_choices, null=True, blank=True)
    Days = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        unique_together = ('buyer', 'address','Days','time')

class PreferredAreaModel(models.Model):
    Time_choices = [
        ('9am-3pm','9am-3pm'),
        ('3pm-9pm', '3pm-9pm'),
    ]
    user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    area=models.CharField(max_length=255, null=True, blank=True)
    time=models.CharField(max_length=255, choices=Time_choices, null=True, blank=True)
    class Meta:
        unique_together = ('user', 'area',)

class ProductModel(models.Model):
    user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=255, null=True, blank=True)
    price=models.IntegerField(null=True, blank=True)
    category=models.CharField(max_length=255, null=False, blank=False,default="")
    image=models.ImageField(null=True,blank=True)
    availQuantity=models.IntegerField(null=True, blank=True)
    refill=models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        unique_together = ('user', 'name',)

    def getProductName (self):
        return self.name

    def getCompany (self):
        return self.user
