from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),

    # user login and logout url
    path('login', login_page, name='login'),
    path('logout', logout_user, name='logout'),

     # customer and company registration url
    path('account/buyer-feed/<str:pk>/', buyer_feed, name='buyer-feed'),
    path('account/company-feed/<str:pk>/', company_feed, name='company-feed'),
    path('account/deliveryMan-feed', deliveryMan_feed, name='deliveryMan-feed'),

    path('company/company-edit-profile', company_edit_profile, name='company-edit-profile'),
    path('customer/customer-edit-profile', buyer_edit_profile, name='buyer-edit-profile'),

     path('post-product/', post_product, name='post-product'),
    path('edit-product/<str:pk>/', edit_product, name='edit-product'),

]+static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)