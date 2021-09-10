import googlemaps
from django.utils.crypto import get_random_string
from .models import *
from users.models import *
import re


def calculateDistance(address1,address2):
    # Requires API key
    if address1 is not None and address2 is not None:
        gmaps = googlemaps.Client(key="AIzaSyCjkI-TzN9giph0DnS1fFF1liDo9HbyQU0")
  
        # Requires cities name
        my_dist = gmaps.distance_matrix(address1,address2)['rows'][0]['elements'][0]
  
        # Printing the result
        #print(my_dist)
        return my_dist['distance']['text']
        #print(my_dist['duration']['text'])

    
def convert(distance):
    #print(distance)
    #print(float(re.findall(r"[-+]?\d*\.\d+|\d+", distance)[0]))
    return float(re.findall(r"[-+]?\d*\.\d+|\d+", distance)[0])
    


def randomCode():

    unique_id = get_random_string(length=6)
    return unique_id

def selectDeliveryMan(order):
    #print(order.product.name,order.buyer)
    companyAddress=order.product.user.companymodel.location
    
    PreferredAreaList=PreferredAreaModel.objects.filter()
    distance={}
    if companyAddress is not None:
        for prefArea in PreferredAreaList:
            if prefArea is not None:
                initialDis=[]
                distanceCompany=convert(calculateDistance(companyAddress,prefArea.area))
                #print('COMPANY',distanceCompany)
                availablityList=AvailabilityModel.objects.filter(buyer=order.buyer)
                #print(prefArea.user, prefArea.area,companyAddress)
           
                for avail in availablityList:
                    if avail is not None:
                        distanceBuyer=convert(calculateDistance(avail.address,prefArea.area))
                        #print('buyer',distanceBuyer)
                        dis=round(distanceBuyer+distanceCompany,2)
                        initialDis.append(dis)
                #print(initialDis)
                        if prefArea.user in distance.keys():
                            if distance[prefArea.user]>min(initialDis):
                                distance[prefArea.user]=min(initialDis)
                        else:
                            distance[prefArea.user]=min(initialDis)
                    else:
                        return None
            
    #print(distance)
    #print(min(distance,key=distance.get))
    if(len(distance)>0):
        return min(distance,key=distance.get)

    else:
        return None
    
   


    
def minDistanceArea(deliveryMan,companyAdress):
    preferredAreaList=PreferredAreaModel.objects.filter(user=deliveryMan)
    distance={}
    #print(companyAdress)
    for prefArea in preferredAreaList:
        if prefArea is not None:
            dis=calculateDistance(prefArea.area,companyAdress)
            if prefArea.area in distance.keys():
                if distance[prefArea.area]>dis:
                    distance[prefArea.area]=dis

            else:
                distance[prefArea.area]=dis
        else:
            return None
    
    #print(distance)     
    #print(min(distance,key=distance.get))
    if(len(distance)>0):
        return min(distance,key=distance.get)

    else:
        return None
