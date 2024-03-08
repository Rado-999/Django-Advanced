from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic as view
from django.views.generic import CreateView


# def create_user_view(request):
#     form = UserCreationForm(request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'form.html', context)


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('auth_user')


user_info = {
    'username': 'Radoslav',
    'password': 'Dimitrov',
    # 'email': 'a'
}


# user = authenticate(**user_info)


def index(request):
    UserModel = get_user_model()
    some_user = UserModel.objects.get(username='Radoslav')
    print(request.user.__class__.__name__)
    print(request.user.__class__.__name__)
    return HttpResponse('aa')


def auth_user(request):
    if request.user.is_authenticated:
        return HttpResponse("user is authenticated")
    else:
        return HttpResponse("not user")


class Usser(view.View):
    form_class = AuthenticationForm
    template_name = "auth_form.html"

    def get(self, request, *args, **kwargs):
        context = {
            'form': self.form_class()
        }
        print(request.user)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        username, password = request.POST['username'], request.POST['password']

        logout(request)
        user = authenticate(username=username, password=password)
        pk = user.pk

        if user is not None:
            login(request, user)
            print(pk)


class LoginUserView(auth_views.LoginView):
    pass


@login_required
def login_with_next_parameter(request):
    return HttpResponse(f"It's a login page for user {request.user} ")
