from rest_framework import serializers
from .models import *



class customerWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = ['custId', 'custFname', 'custLname', 'custEmail','custPhone', 'address', 'products', 'expiryDate','amount','itemQuantity', 'message', 'createdAt']
        read_only_fields = ['custId','createdAt']


class customerReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = ['custId', 'custFname', 'custLname', 'custEmail','custPhone', 'address', 'products', 'expiryDate','itemQuantity', 'amount', 'message', 'createdAt']
        read_only_fields = ['custId','createdAt']
        depth = 2