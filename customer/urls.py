from django.urls import path
from .views import *

urlpatterns = [
    path('',createCustomer.as_view()),
    path('/<uuid:custId>',customerAPIView.as_view()),
    path('/exportCustomer/<str:token>',downloadCustomer),
    path('/getSales',getSales),
    path('/getTotlalAmount',getAllAmount),
    path('/today',customerToday),

]