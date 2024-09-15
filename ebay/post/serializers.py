from .models import *
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

class PostCreatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'description', 'price', 'category', 'image']

    def validate(self, attrs):
        price = attrs.get('price')
        if price is not None and price <= 0:
            raise serializers.ValidationError('Price must be greater than 0')
        return attrs
    
class MessageSerializer(serializers.Serializer):
    content = serializers.CharField()
    post = serializers.IntegerField()
    def validate(self, attrs):
        post = attrs.get('post')
        if not Post.objects.filter(id=post).exists():
            raise serializers.ValidationError('Post does not exist')
        return attrs
    
class SellerMessageSerializer(serializers.Serializer):
    content = serializers.CharField()
    post = serializers.IntegerField()
    message_session = serializers.IntegerField()
    def validate(self, attrs):
        post = attrs.get('post')
        if not Post.objects.filter(id=post).exists():
            raise serializers.ValidationError('Post does not exist')
        return attrs

class ViewMessagesSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["content", "sender", 'timestamp']

class MessageSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageSession
        fields = "__all__"