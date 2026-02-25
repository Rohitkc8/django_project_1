from django.urls import path
from .views import *

urlpatterns = [
    path("",Login_page),
    path("logout/",Logout_user),
    path("signup/",Signup_user),
]