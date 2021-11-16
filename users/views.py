from django.views import View
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from . import forms

# Create your views here.
class LoginView(FormView):

    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authentiacate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


def log_out(self):
    logout(request)
    return redirect(reverse("core:home"))


class SignUpView(FormView):
    temlplate_name = "users/signup.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")
    initial = {
        "first_name": "길동",
        "last_name": "홍",
        "email": "itn@las.com",
        "password": "1234",
        "password1": "1234",
    }

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authentiacate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
        return super().form_valid(form)
