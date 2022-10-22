import os

from django.shortcuts import render, redirect
from django.contrib import auth
from django.views.generic import CreateView, FormView
from .forms import *


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'account/register.html'
    success_url = '/'


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'account/login.html'
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = auth.authenticate(self.request, username=username, password=password)
        if user:
            auth.login(self.request, user)
        return super().form_valid(form)


def logout(request):
    auth.logout(request)
    return redirect('/')

def kakao_login(request):
    app_rest_api_key = os.environ.get("KAKAO_REST_API_KEY")
    redirect_uri = main_domain + "users/test/kakao/callback"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={'06c8f6f94735dc0f8b96723b2c3f2639'}$redirect_url={''}"
    )