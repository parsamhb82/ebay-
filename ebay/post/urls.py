from .views import *
from django.urls import path

urlpatterns = [
    path('post-list/', PostList.as_view()), #check
    path('post-create/', PostCreate.as_view()), #check
    path('post-update/<int:pk>/', PostUpdate.as_view()),#check
    path('category-create/', CreatCategory.as_view()),#check
    path('all-available-post/', AllAvailablePost.as_view()),#check
    path('customer-send-message/', CustomerSendMessage.as_view()),#check
    path('seller-send-message/', SellerSendMessage.as_view()),#check
    path('view-messages/<int:message_session_id>/', MessagesInSessionView.as_view()),#check
    path('view-messages-session/', ViewOwnSessions.as_view()),#check
    path('view-own-post/', ViewOwnPost.as_view()),#check
    path('retrieve-post/<int:pk>/', RetrievePost.as_view()),#check
]
