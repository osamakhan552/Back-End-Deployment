from django.urls import path
from .views import *

urlpatterns = [
    path('',createCustomer.as_view()),
    path('/<uuid:custId>',customerAPIView.as_view()),
]