from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .permissions import IsSuperUser
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response


class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsSuperUser]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['price']
    search_fields = ['category__name']
    filterset_fields = ['category__name', 'title']

class PostCreate(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreatSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user.customer, image=self.request.FILES.get('image', ''))

class PostUpdate(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreatSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(seller=self.request.user.customer)
class ViewOwnPost(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['price', 'created_at']
    search_fields = ['title']
    filterset_fields = ['category__name', 'title']

    def get_queryset(self):
        return Post.objects.filter(seller=self.request.user.customer)
class RetrievePost(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(seller=self.request.user.customer)

class CreatCategory(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsSuperUser]

from rest_framework.views import APIView
from rest_framework import status
class CustomerSendMessage(APIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        post = Post.objects.get(id=request.data['post'])

        # Check if the message session exists and user is not the seller
        if post.seller != request.user.customer:
            session_exists = MessageSession.objects.filter(customer=request.user.customer, post=post).exists()
            
            # Create a message session if it doesn't exist
            if not session_exists:
                message_session = MessageSession.objects.create(customer=request.user.customer, post=post)
            else:
                message_session = MessageSession.objects.get(customer=request.user.customer, post=post)
            
            Message.objects.create(
                sender=request.user.customer,
                content=request.data['content'],
                message_session=message_session
            )
            
            return Response({'message': 'Message sent successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'You cannot send a message to yourself'}, status=status.HTTP_400_BAD_REQUEST)
class SellerSendMessage(APIView):
    serializer_class = SellerMessageSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        post = Post.objects.get(id=request.data['post'])
        message_session = MessageSession.objects.get(id=request.data['message_session'], post=post)

        # Create the message
        Message.objects.create(
            sender=request.user.customer,
            content=request.data['content'],
            message_session=message_session
        )
        
        return Response({'message': 'Message sent successfully'}, status=status.HTTP_201_CREATED)
class MessagesInSessionView(APIView):
    serializer_class = ViewMessagesSerilizer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    def get(self, request,message_session_id ,*args, **kwargs):
        messages = Message.objects.filter(message_session_id=message_session_id).order_by('-timestamp')

        if not messages.exists():
            return Response({"detail": "No messages found for this session."}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(messages, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
class AllAvailablePost(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['price']
    search_fields = ['category__name']
    filterset_fields = ['category__name', 'title']
    def get_queryset(self):
        return Post.objects.filter(is_done=False)
    
from django.db.models import Q
class ViewOwnSessions(ListAPIView):
    serializer_class = MessageSessionSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
            return MessageSession.objects.filter(
                Q(customer=self.request.user.customer) | Q(post__seller=self.request.user.customer)
        ).order_by("-created_at")    

