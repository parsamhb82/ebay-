from django.shortcuts import render
from .serializers import CustomerRegisterSerializer, CustomerSerializer
from .models import Customer
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

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

class UpdateUserView(CreateAPIView):
    serializer_class = CustomerRegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        customer = Customer.objects.create(user=user, phone=request.data['phone'], address=request.data['address'], city=request.data['city'])
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

class RetriveUserView(CreateAPIView):
    serializer_class = CustomerRegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        customer = Customer.objects.create(user=user, phone=request.data['phone'], address=request.data['address'], city=request.data['city'])
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

class CustomerDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        customer = get_object_or_404(Customer, user=request.user)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        customer = get_object_or_404(Customer, user=request.user)
        serializer = CustomerSerializer(customer, data=request.data, partial=True)  # Partial update allowed
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)