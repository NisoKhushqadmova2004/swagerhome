from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import CustomUser
from .serializers import RegisterSerializer, LoginSerializer


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username,password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh),'access': str(refresh.access_token)})
        return Response({'error': 'Username ё password нодуруст аст'},status=status.HTTP_400_BAD_REQUEST)

class RefreshView(generics.GenericAPIView):
    def post(self, request):
        refresh = request.data.get('refresh')
        try:
            token = RefreshToken(refresh)
            return Response({'access': str(token.access_token)})
        except Exception:
            return Response({'error': 'Refresh token нодуруст аст'},status=status.HTTP_400_BAD_REQUEST)   

class LogoutView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    def post(self, request):
        refresh = request.data.get('refresh')
        try:
            token = RefreshToken(refresh)
            token.blacklist()
            return Response({'message': 'Logout шуд'})
        except Exception:
            return Response({'error': 'Token нодуруст аст'},status=status.HTTP_400_BAD_REQUEST)
