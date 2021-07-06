from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(BuyerModel)
admin.site.register(CompanyModel)
admin.site.register(DeliveryManModel)
admin.site.register(AddressPhoneModel)
admin.site.register(TimeSlotModel)
admin.site.register(AvailabilityModel)