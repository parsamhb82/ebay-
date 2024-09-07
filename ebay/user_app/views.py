from django.shortcuts import render
from .serializers import CustomerRegisterSerializer
from .models import Customer
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

class Login(TokenObtainPairView):
    pass

class RefreshToken(TokenRefreshView):
    pass

class UserRegistrationView(CreateAPIView):
    serializer_class = CustomerRegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        customer = Customer.objects.create(user=user, phone=request.data['phone'], address=request.data['address'], city=request.data['city'])
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)