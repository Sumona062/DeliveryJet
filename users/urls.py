from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
from order.urls import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),

    # user login and logout url
    path('login', login_page, name='login'),
    path('logout', logout_user, name='logout'),

     
    path('account/buyer-feed/<str:pk>/', buyer_feed, name='buyer-feed'),
    path('account/company-feed/<str:pk>/', company_feed, name='company-feed'),
     path('account/company-feed-category/<str:pk>/<str:cat>/', company_feed_category, name='company-feed-category'),
    path('account/deliveryMan-feed/<str:pk>/', deliveryMan_feed, name='deliveryMan-feed'),
    
    path('company/company-edit-profile', company_edit_profile, name='company-edit-profile'),
    path('customer/customer-edit-profile', buyer_edit_profile, name='buyer-edit-profile'),
    path('customer/add-address', add_availability, name='add-availability'),
    path('customer/edit-address/<str:pk>/', edit_availability, name='edit-availability'),
    path('deliveryMan/deliveryMan-edit-profile', deliveryMan_edit_profile, name='deliveryMan-edit-profile'),
    path('delete-preferredArea/<str:pk>/', delete_preferredArea, name='delete-preferredArea'),

    path('post-product/', post_product, name='post-product'),
    path('edit-product/<str:pk>/', edit_product, name='edit-product'),

    # utilities
    path('account-settings/<str:pk>/', account_settings, name='account-settings'),

    path('account/buyer-feed/<str:pk>/view_cart', view_cart, name='view-cart'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)