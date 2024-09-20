from .views import (Login,
                    RefreshToken,
                    UserRegistrationView,
                    CustomerDetailView,
                    UpdateUserView,
                    RetrieveUserView
                    )
from django.urls import path

urlpatterns = [
    path('login/', Login.as_view()),#check
    path('refresh/', RefreshToken.as_view()),#check
    path('register/', UserRegistrationView.as_view()),#check
    path('customer/', CustomerDetailView.as_view()),#check
    path('update/<int:pk>', UpdateUserView.as_view()),#check
    path('retrieve/<int:pk>', RetrieveUserView.as_view()),#check
    path('customer/<int:pk>', CustomerDetailView.as_view())


]