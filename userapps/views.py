from rest_framework.views import APIView
from rest_framework import status,serializers
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout

from . serializers import *
from . models import *


# Create your views here.
class RegisterUserView(APIView):
    def post(self,request):
        try:
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_500_BAD_REQUEST)
        
class LoginUserView(APIView):
    def post(self,request):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return Response({"message":"User Logged In"}, status=status.HTTP_200_OK)
            return Response({"error":"Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_500_BAD_REQUEST)
        
class LogoutUserView(APIView):
    def post(self,request):
        try:
            logout(request)
            return Response({"message":"User Logged Out"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_500_BAD_REQUEST)
            