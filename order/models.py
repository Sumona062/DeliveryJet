from django.db import models
from users.models import *

class OrderModel(models.Model):
    buyer = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, null=True, blank=True, on_delete=models.CASCADE)
    count=models.IntegerField(null=False,blank=False,default=0)
    total=models.IntegerField(null=False,blank=False,default=0)

    class Meta:
        unique_together = ('buyer', 'product',)

class OrderScheduleModel(models.Model):
    order=models.ForeignKey(OrderModel, null=True, blank=True, on_delete=models.CASCADE,unique=True)
    code=models.IntegerField(null=False,blank=False,default=0)
    deliveryMan=models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

