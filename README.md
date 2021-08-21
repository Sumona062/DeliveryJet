# DeliveryJet

# 1. Clone project
> Make sure you have already installed python3 and git.
```
https://github.com/Sumona062/DeliveryJet.git
```
# create virtual environment 
```
-python -m venv ENV
```
# start virtual environment 
```
-.\ENV\Scripts\activate
```


# go to inside the project
```
-cd DeliveryJet
```
# install
```
-python -m pip install django
-python -m pip install pillow
-python -m pip install django-ckeditor
-python -m pip install django-filter
-python -m pip install django-widget-tweaks
```
# run the server
```
-python .\manage.py runserver
```

# Phase-1
```
-Sign Up
-Log In
-Company Feed,Customer Feed
-Edit company,Customer profile
-Post product
-Edit Product
-Account Settings
```
# Phase-2
```
### Features
-Delivery Man Feed
-Edit DeliveryMan Profile
-Add to cart
-Edit Cart
-View Cart
-Add and Delete Availability Address-time slot
-Add and Delete Preferred Area
```
#### Unit Test
```
--Model Test
-ProductModelTestCase
-CompanyModelTestCase
-DeliveryManModelTestCase
-BuyerModelTestCase
--Views Text
-CompanyFeedTestCase
-CompanyFeedCategoryTestCase
```