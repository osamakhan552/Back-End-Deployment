from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics,status,filters
from .models import *
from .serializer import *
from product.models import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class createCustomer(generics.ListCreateAPIView):
    authorization_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = customer.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['^custFname','^custEmail','^custPhone']
    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return customerWriteSerializer
        else:
            return customerReadSerializer

    def post(self, request,format = None):
        if int(request.data['itemQuantity']) <= int(product.objects.get(prodId = request.data['products']).quantity):
            print(request.data['message'])
            customer = customerWriteSerializer(data = request.data)
            
            print(customer.is_valid())
            if customer.is_valid():
                customer.save()
                return Response(customer.data,status = status.HTTP_201_CREATED)
        return Response({'message':"error"},status = status.HTTP_400_BAD_REQUEST)


class customerAPIView(generics.RetrieveUpdateDestroyAPIView):
    authorization_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = "custId"
    queryset = customer.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return customerWriteSerializer
        else:
            return customerReadSerializer
