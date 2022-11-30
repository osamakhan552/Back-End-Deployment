from rest_framework import serializers
from .models import *

class productReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = ['createdAt','prodId','prodNumber','prodName','amount','quantity']
        read_only_fields = ['createdAt','prodId']
        depth=1

class productWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = ['createdAt','prodId','prodNumber','prodName','amount','quantity']
        read_only_fields = ['createdAt','prodId']
        

