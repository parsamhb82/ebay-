from .views import *
from django.urls import path

urlpatterns = [
    path('post-list/', PostList.as_view()), #check
    path('post-create/', PostCreate.as_view()), #check
    path('post-update/<int:pk>/', PostUpdate.as_view()),#check
    path('category-create/', CreatCategory.as_view()),#check
    path('message-create/', CreatMessage.as_view()),#check
    path('reciever-message-list/', RecieverMessageView.as_view()),#check
    path('sender-message-list/', SenderMessageView.as_view()),#check
    path('all-available-post/', AllAvailablePost.as_view()),#check




]