from django.views import View
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from . import forms, models

import os
import request

# Create your views here.
class LoginView(FormView):

    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        form.save()
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
        user.verfy_email(0)
        return super().form_valid(form)


def complete_verification(request, key):
    try:
        user = models.User.objects.get(email_secret=key)
        user.email_verified = True
        user.email_secret = ""
        user.save()
        # todo : add succeess message
    except models.User.DoesNotExist:
        # todo : add error message
        pass
    return redirect(reverse("core:home"))


def github_login(request):
    client_id = os.environ.get("GH_ID")
    redirect_uri = "http://127.0.0.1:8000/users/login/github/callback"
    return redirect(
        f"https://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}"
    )


def github_Callback(request):
    client_id = os.environ.get("GH_ID")
    client_secret = os.environ.get("GH_SECRET")
    code = requset.GET.get("code", None)
    if code is not None:
        request = requests.post(
            f"https://github/login/oauth/access_token?client_id={client_id}&client_secret={client_secret}&code={code}",
            headers={"Accept": "application/json"},
        )
        result_json = result.json()
        error = result_json.get("error", None)
        if error is not None:
            return redirect(reverse("users:login"))
        else:
            access_token = result_json.get("acess_token")
            api_requset = requests.get(
                "https://api.github.com/user",
                headers={
                    "Authorization": f"token {access_token}",
                    "Accept": "application/json",
                },
            )
            username = profile_request.json("login", None)
            profille_json = profile_request.json()
            if username is not None:
                name = profile_json.get("name")
                email = profile_json.get("email")
                bio = profile_json.get("bio")
                user=models.User.objects.get(email=email)
                if user in not None:
                    return redirect(reverse("users:login"))
                else:
                    user=models.User.objects.create(username=email,first_name=name,bio=bio,email=email)
                    login(rquest,user)
                    return redirect(reverse("core:home"))
            else:
                
                return redirect(reverse("users:login"))
    else:
        return redirect(reverse("core:home"))
