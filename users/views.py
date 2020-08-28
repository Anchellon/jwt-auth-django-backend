from django.shortcuts import render
from users.serializers import MyUserSerializer,MyUserInfoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import MyUser
# Create your views here.

class UserList(APIView):
    """
    List all users, or create a new user.
    """
    def get(self, request, format=None):
        users = MyUser.objects.all()
        serializer = MyUserInfoSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MyUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)