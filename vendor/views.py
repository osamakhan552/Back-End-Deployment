from django.shortcuts import render
from rest_framework import status,generics,filters
from rest_framework.response import Response
from .serializer import *
from .serializer import orderReceivedReadSerializer
from .models import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes,action



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
            print("in orderReceivedApiView.................................")
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
        for i in allOrder:
            for j in recievedOrder:
                if i.orderId == j.orderNumber.orderId:
                    res = {
                        'orderId':i.orderId,
                        'orderNumber':i.orderNumber,
                        'materialNumber':i.materialNumber,
                        'orderQuantity':i.orderQuantity,
                        'vendorCode':i.vendorCode,
                        'orderDelivery':i.orderDelivery,
                        'createdAt':i.createdAt

                    }
                    myData = orderReadSerializer(res)
                    
                    lst.append(myData.data)
        print(lst)
        return Response({'msg':lst},status=status.HTTP_202_ACCEPTED)
