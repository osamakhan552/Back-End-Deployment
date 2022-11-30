from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework import status,generics,filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class usersListAPIView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self,*args, **kwargs):
        return employee.objects.all().filter(is_active=True,is_superuser=False)

    filter_backends = [filters.SearchFilter]
    search_fields = ['^email','^empCbid','^empFname','^username']
    
    def post(self, request, format = None):
        print("ROLES: ")
        print(roles.objects.get(roleId = request.data['roleId']).roleName)
        user = employeeWriteSerializer(data=request.data)

        if user.is_valid():
            user.save()
            current_user = employee.objects.get(username = request.data['username'])
            current_user.set_password(request.data['password'])
            current_user.save()
            print("saved!!")
            return Response(user.data,status = status.HTTP_201_CREATED)
        return Response(user.errors, status = status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        method = self.request.method
        if method == 'POST' or method == 'PUT':
            return employeeWriteSerializer
        else:
            return employeeReadSerializer

#retrieve Update and delete current user
class userAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
   
    lookup_url_kwarg = 'pk'
    queryset = employee.objects.all()
    def put(self, request, *args, **kwargs):
        request.data.pop('username')
        request.data.pop('password')
        return self.update(request, *args, **kwargs)
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save() 
        return Response(status=status.HTTP_204_NO_CONTENT)
    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return employeeWriteSerializer
        else:
            return employeeReadSerializer
       
class rolesListAPIView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = roles.objects.all()
    #serializer_class = roleWriteSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['^roleName']
    def post(self, request, *args, **kwargs):
      
        return self.create(request, *args, **kwargs)
    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return roleWriteSerializers
        else:
            return roleReadSerializers 

class rolesAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = roles.objects.all()
    #serializer_class = roleWriteSerializers
    lookup_url_kwarg = 'pk'
    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return roleWriteSerializers
        else:
            return roleReadSerializers