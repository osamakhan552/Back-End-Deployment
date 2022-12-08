from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics,status,filters
from rest_framework.decorators import api_view,authentication_classes, permission_classes
from MyInventory.utils import QuerysetToXLSX
from .models import *
from .serializer import *
from product.models import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import datetime
from datetime import date

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


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def getSales(request,format = None):

    if request.method == "GET":
        allCustomer = customer.objects.all()
        prodList  = {}
   
        for cust in allCustomer:
            if str(cust.products.prodName) in prodList:
                prodList[str(cust.products.prodName)] = prodList[str(cust.products.prodName)]+1
            else:
                prodList[str(cust.products.prodName)] = 1
        res = []
        for k,v in prodList.items():
            temp = {
                "product":k,
                "count":v
            }
            res.append(temp)
 
        return Response({"results":res,"count":len(res)},status = status.HTTP_200_OK)
    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def getAllAmount(request,format = None):

    if request.method == "GET":
        allCustomer = customer.objects.all()
     
        saleList = {}
        
        for cust in allCustomer:
         
            if str(cust.products.prodName) in saleList:
                saleList[str(cust.products.prodName)] = int(cust.products.amount)+saleList[str(cust.products.prodName)]
            else:
                saleList[str(cust.products.prodName)] = int(cust.products.amount)
        res = []
        for k,v in saleList.items():
            temp = {
                "product":k,
                "amount":v
            }
            res.append(temp)
         
        return Response({"results":res,"count":len(res)},status = status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def customerToday(request,format = None):

    if request.method == "GET":
        allCustomer = customer.objects.all()
        CustomerCount = 0
        for cust in allCustomer:
            if cust.createdAt.strftime("%Y-%m-%d") == date.today().strftime("%Y-%m-%d"): CustomerCount = CustomerCount + 1
        return Response({"results":CustomerCount},status = status.HTTP_200_OK)
    


@api_view(['GET'])
def downloadCustomer(request,token,format = None):
    columns = ["First Name","Last Name","Email","Phone","Address","product","amount",'item Quantity'] 
    rows = customer.objects.all().values_list('custFname','custLname','custEmail',"custPhone","address","products__prodName","amount","itemQuantity")
    sheet = QuerysetToXLSX(columns,rows,"Customers",token)
    return sheet.convert
