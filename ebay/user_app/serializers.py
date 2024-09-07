from .models import Customer
from django.contrib.auth.models import User
from rest_framework import serializers
class CustomerRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    phone = serializers.CharField(max_length=10)
    address = serializers.CharField(max_length=500)
    city = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'password', 'phone', 'address', 'city', 'email', 'first_name', 'last_name']
    
    def create(self, validated_data):
        return User.objects.create_user(username= validated_data['username'], 
                                        password=validated_data['password'], 
                                        email=validated_data['email'], 
                                        first_name=validated_data['first_name'], 
                                        last_name=validated_data['last_name'])