from django.urls import path
from .views import UserCreate, LoginView
from rest_framework.authtoken import views

urlpatterns = [
    path("register/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
]