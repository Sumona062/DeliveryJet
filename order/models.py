from enum import unique
from django.db import models
from users.models import *

class OrderModel(models.Model):
    buyer = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, null=True, blank=True, on_delete=models.CASCADE)
    count=models.IntegerField(null=False,blank=False,default=0)
    total=models.IntegerField(null=False,blank=False,default=0)
    status=models.CharField(max_length=10,null=False,blank=False,default="not checkout")

    class Meta:
        unique_together = ('buyer', 'product','status')

class OrderScheduleModel(models.Model):
    order=models.OneToOneField(OrderModel, null=True, blank=True, on_delete=models.CASCADE)
    code=models.CharField(max_length=6,null=True,blank=False)
    postDate=models.DateField(null=True,blank=False)
    deliveryMan=models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

   
