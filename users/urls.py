from django.urls import path
from . import views

app_name = "users"

urlpartters = [
    path("login", views.LoginView.as_view(), name="login"),
    path("login/github", views.github_login, name="github-login"),
    path("login/github/callback", views.github_callback, name="github-callback"),
    path("logout", views.logout, name="logout"),
    path("signup", views.SignUpView.as_view, name="sign up"),
    path("verify/<str:key>", views.complete_verification, name="complete-verification"),
\]
http://127.0.0.1:8000/users/login/github/callback