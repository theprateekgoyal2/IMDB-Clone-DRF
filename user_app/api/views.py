from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import RegistrationSerializer
from rest_framework_simplejwt.tokens import RefreshToken
# from user_app import models

@api_view(['POST',])
def registeration_view(request):
    serializer = RegistrationSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        account = serializer.save()
        data['Message'] = 'Registration Sucessful'
        data['username'] = account.username
        data['email'] = account.email

        refresh = RefreshToken.for_user(account)
        # token = Token.objects.get(user=account)
        # print(type(str(token)))
        data['token'] = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    else: 
        data = serializer.errors
    
    return Response(data, status.HTTP_201_CREATED)

@api_view(['POST',])
def logout_view(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)