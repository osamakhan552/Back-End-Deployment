from django.urls import path,include
from .views import *


urlpatterns = [
    path('',usersListAPIView.as_view()),
    path('/<uuid:pk>',userAPIView.as_view()),
    path('/roles/<uuid:pk>',rolesAPIView.as_view()),
    path('/roles',rolesListAPIView.as_view()),
]