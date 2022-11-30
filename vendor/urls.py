from django.urls import path
from .views import *

urlpatterns = [
    path('',createVendor.as_view()),
    path('/<uuid:vendorId>',vendorApiView.as_view()),
    path('/orders',createOrder.as_view()),
    path('/orderReceived',createOrderReceived.as_view()),
    path('/orders/<uuid:orderId>',orderApiView.as_view()),
    path('/orderReceived/<uuid:orderNumber>',orderReceivedApiView.as_view()),
    path('/receivedOrder',onlyReceivedOrder),
]