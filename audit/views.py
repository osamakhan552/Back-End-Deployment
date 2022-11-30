from django.shortcuts import render
from rest_framework import status,generics,filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializer import *

class auditList(generics.ListCreateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = audit.objects.all()
    serializer_class = auditSerializer



class auditTypeList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = auditType.objects.all()
    serializer_class = auditTypeSerializer

