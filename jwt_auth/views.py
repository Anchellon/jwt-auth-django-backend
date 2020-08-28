

# Create your views here.

from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated 
  
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class HelloView(APIView): 
    permission_classes = (IsAuthenticated, ) 
  
    def get(self, request): 
        content = {'message': 'Hello, GeeksforGeeks'} 
        return Response(content) 
