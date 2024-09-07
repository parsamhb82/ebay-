from .views import (Login,
                    RefreshToken,
                    UserRegistrationView,
                    CustomerDetailView
                    )
from django.urls import path

urlpatterns = [
    path('login/', Login.as_view()),#check
    path('refresh/', RefreshToken.as_view()),#check
    path('register/', UserRegistrationView.as_view()),#check
    path('customer/', CustomerDetailView.as_view()),#check


]