from django.urls import path,include
from .views import *

urlpatterns = [
    path('',createProduct.as_view()),
    path('/<uuid:prodId>',productAPIView.as_view()),
]

