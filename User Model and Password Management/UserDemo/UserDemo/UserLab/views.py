from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from UserDemo.UserLab import forms


# Create your views here.
def page(request):
    return render(request, 'UserLab/home.html')


def loginpage(request):
    pass


class RegisterForm(CreateView):
    template_name = 'UserLab/register_page.html'
    success_url = reverse_lazy('profile')
    form_class = forms.RegistrationForm




def profile(request):
    return HttpResponse('proifle')
