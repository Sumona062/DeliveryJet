from django.urls import path
from .views import *
from users.urls import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('account/buyer-feed/<str:pk>/view_cart', view_cart, name='view-cart'),
    path('account/buyer-feed/<str:pk>/view_pending', view_pending, name='view-pending'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)