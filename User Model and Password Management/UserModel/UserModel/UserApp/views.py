from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView

from UserModel.UserApp import models
from UserModel.UserApp.forms import UserRegistrationForm, UserRegistrationForm2



# Create your views here.
def index(request):
    return render(request, 'index.html')


# class RegistrationView(View):
#     template_name = 'registration.html'
#
#     def get(self, request):
#         form = UserRegistrationForm()
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request):
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#         return render(request, 'index.html')


class RegistrationView2(CreateView):
    template_name = 'registration2.html'
    form_class = UserRegistrationForm2
    success_url = reverse_lazy('profile')


class LoginUserView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('profile')


UserModel = get_user_model()


class UserDetailsView(DetailView):
    model = UserModel
    template_name = 'about_me.html'
    context_object_name = 'user'


class LogoutUserView(LogoutView):
    next_page = '/custom-logout-page/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next_page'] = self.next_page



def profile(request):
    return render(request, 'user_profile.html')
