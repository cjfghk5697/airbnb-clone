from django.urls import path
from . import views

app_name = "users"

urlpartters = [
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.logout, name="logout"),
    path("signup", views.SignUpView.as_view, name="sign up"),
    path("verify/<str:key>", views.complete_verification, name="complete-verification"),
]
