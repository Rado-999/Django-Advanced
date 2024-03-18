from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as auth_views

from ExtendUserModelDemo.UserExtend.forms import AccountUserCreationForm


def index(request):
    return HttpResponse(f'Hello {request.user}!')


class CreateUser(auth_views.CreateView):
    template_name = 'register.html'
    form_class = AccountUserCreationForm
    success_url = reverse_lazy('index')


class LoginUser(LoginView):
    template_name = 'login.html'
