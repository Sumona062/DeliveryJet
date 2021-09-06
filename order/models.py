from enum import unique
from django.db import models
from users.models import *

class OrderModel(models.Model):
    buyer = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel,null=True,  on_delete=models.CASCADE)
    count=models.IntegerField(null=False,blank=False,default=0)
    total=models.IntegerField(null=False,blank=False,default=0)
    status=models.CharField(max_length=10,null=False,blank=False,default="not checkout")

    class Meta:
        unique_together = ('buyer', 'product','status')

    def getBuyer(self):
        return self.buyer

class OrderScheduleModel(models.Model):
    order=models.OneToOneField(OrderModel,null=True, on_delete=models.CASCADE)
    code=models.CharField(max_length=6,default="")
    postDate=models.CharField(max_length=100,default="")
    deliveryMan=models.ForeignKey(User, null=True,on_delete=models.CASCADE)
    is_marked=models.BooleanField(default=False)

    def getOrder(self):
        return self.order


   
