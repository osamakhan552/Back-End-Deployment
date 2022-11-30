from rest_framework import serializers
from .models import *
from product.models import product
from product.serializer import productWriteSerializer,productReadSerializer

class vendorWriteSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = VendorMaster
        fields = ['createdAt','vendorId','vendorCode','vendorName','vendorAddress','vendorPrimaryEmail','vendorPrimaryPhone','vendorPrimaryName','vendorSecondaryEmail','vendorSecondaryPhone','products']
        read_only_fields = ['createdAt','vendorId']
      

   

class orderWriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = ['createdAt','orderId','orderNumber','prodNumber','orderQuantity','vendorCode','orderDelivery','status']
        read_only_fields = ['createdAt','orderId']


class orderReceivedWriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderReceived
        fields = ['createdAt','orderNumber','quantityReceived', 'orderReceiveDate']
        read_only_fields = ['createdAt','orderReceiveDate']

class vendorReadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VendorMaster
        fields = ['createdAt','vendorId','vendorCode','vendorName','vendorAddress','vendorPrimaryEmail','vendorPrimaryPhone','vendorPrimaryName','vendorSecondaryEmail','vendorSecondaryPhone','products']
        read_only_fields = ['createdAt','vendorId']
        depth = 2


class orderReadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = ['createdAt','orderId','orderNumber','prodNumber','orderQuantity','vendorCode','orderDelivery','status']
        read_only_fields = ['createdAt','orderId']
        depth = 1

class orderReceivedReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderReceived
        fields = ['createdAt','orderNumber','quantityReceived', 'orderReceiveDate']
        read_only_fields = ['createdAt','orderReceiveDate']
        depth = 2