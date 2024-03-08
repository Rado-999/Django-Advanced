from django.urls import path

from UserModel.UserApp import views
from UserModel.UserApp.views import RegistrationView2, LoginUserView, profile, UserDetailsView

urlpatterns = [
    path('', views.index, name='index'),
    path('register2', RegistrationView2.as_view(), name='register2'),
    path('login', LoginUserView.as_view(), name='login'),
    path('profile', profile, name='profile'),
    path('profile/about/<int:pk>/',UserDetailsView.as_view(), name='profile-about')

]
