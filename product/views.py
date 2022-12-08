from django.shortcuts import render
from rest_framework import status,generics,filters
from rest_framework.response import Response

from MyInventory.utils import QuerysetToXLSX
from .serializer import *
from .models import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,authentication_classes, permission_classes



class createProduct(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['^prodName','^prodNumber']

    queryset = product.objects.all()
    serializer_class = productWriteSerializer


class productAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = "prodId"
    queryset = product.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return productWriteSerializer
        else:
            return productReadSerializer




@api_view(['GET'])
def downloadProduct(request,token,format = None):
    columns = ["Material Number","Material Name" ,"Amount"] 
    rows = product.objects.all().values_list('prodNumber','prodName','amount')
    sheet = QuerysetToXLSX(columns,rows,"Product",token)
    return sheet.convert
