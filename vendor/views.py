from django.shortcuts import render
from rest_framework import status,generics,filters
from rest_framework.response import Response
from .serializer import *
from .serializer import orderReceivedReadSerializer
from .models import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes,action
from MyInventory.utils import *


class createVendor(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['^vendorName','^vendorCode']

    queryset = VendorMaster.objects.all()
    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return vendorWriteSerializer
        else:
            return vendorReadSerializer
            



class createOrder(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['^orderNumber','^vendorCode']
    queryset = Order.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return orderWriteSerializer
        else:
            return orderReadSerializer


class createOrderReceived(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = OrderReceived.objects.all()

    filter_backends = [filters.SearchFilter]

    search_fields = ['^orderNumber']

    def get_serializer_class(self):
        method = self.request.method
        print("method: "  + method)
        if method == 'PUT' or method == 'POST':
            return orderReceivedWriteSerializer
        else:
         
            return orderReceivedReadSerializer



class vendorApiView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication ]
    permission_classes = [IsAuthenticated]
    lookup_field = 'vendorId'
    queryset = VendorMaster.objects.all()
    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return vendorWriteSerializer
        else:
            return vendorReadSerializer


class orderApiView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication ]
    permission_classes = [IsAuthenticated]
    #serializer_class = OrderSerializer
    lookup_field = 'orderId'
    queryset = Order.objects.all()
    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return orderWriteSerializer
        else:
            return orderReadSerializer


class orderReceivedApiView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication ]
    permission_classes = [IsAuthenticated]
    #serializer_class = OrderSerializer
    lookup_field = 'orderNumber'
    queryset = OrderReceived.objects.all()
    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return orderReceivedWriteSerializer
        else:
            return orderReceivedReadSerializer

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def onlyReceivedOrder(request,format = None):

    if request.method == 'GET':

        allOrder = Order.objects.all()
        recievedOrder = OrderReceived.objects.all()
        res = {}
        lst = []
        receivedList = []
   
        for j in recievedOrder:
            receivedList.append(str(j.orderNumber.orderId))
            print("IN REC: "  + str(j.orderNumber.orderId))
    
        for i in allOrder:
            if str(i.orderId) not in receivedList:
                # print(i.prodNumber.prodName)
                print("IN ORDER: " + str(i.orderId))
                res = {
                    'orderId':i.orderId,
                    'orderNumber':i.orderNumber,
                    'prodNumber':i.prodNumber,
                    'orderQuantity':i.orderQuantity,
                    'vendorCode':i.vendorCode,
                    'orderDelivery':i.orderDelivery,
                    'createdAt':i.createdAt,
                    'status':i.status
                }
                myData = orderReadSerializer(res)
                
                lst.append(myData.data)
    
        return Response({'results':lst,'count':len(lst)},status=status.HTTP_200_OK)


@api_view(['GET'])
def downloadVendor(request,token,format = None):
    columns = ["Code","Name","Address","Primary Name" ,"Primary Email", "Primary Phone","Secondary Email","Secondary Phone","Materials"] 
    rows = VendorMaster.objects.all().values_list('vendorCode','vendorName','vendorAddress','vendorPrimaryName','vendorPrimaryEmail','vendorPrimaryPhone','vendorSecondaryEmail','vendorSecondaryPhone','products__prodName')
    sheet = QuerysetToXLSX(columns,rows,"Vendors",token)
    return sheet.convert

@api_view(['GET'])
def downloadOrders(request,token,format = None):
    columns = ["Order Number","Material Number","Order Quantity" ,"Vendor Code" ,"Order Delivery Date","Created At"] 
    rows = Order.objects.all().values_list('orderNumber','prodNumber__prodNumber','orderQuantity','vendorCode__vendorCode','orderDelivery','createdAt')
    sheet = QuerysetToXLSX(columns,rows,"Orders",token)
    return sheet.convert

@api_view(['GET'])
def downloadOrderReceived(request,token,format = None):
    columns = ["Order Number","Quantity Received" ,"Receive Date"] 
    rows = OrderReceived.objects.all().values_list('orderNumber__orderNumber','quantityReceived','orderReceiveDate')
    sheet = QuerysetToXLSX(columns,rows,"OrderReceived",token)
    return sheet.convert
