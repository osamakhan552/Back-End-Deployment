from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from datetime import datetime,timedelta, timezone
from rest_framework import status
import jwt
from rest_framework.response import Response
from rest_framework.views import APIView


class CustomAuthToken(ObtainAuthToken):
      
  def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        print("MY TOKEN :",token)
        return Response({
            'msg' : 'Success',
            'token': token.key,
            'userId': user.pk,
            'email': user.email,
            'role':user.roleId.roleName,
            'name':user.empFname
        })

