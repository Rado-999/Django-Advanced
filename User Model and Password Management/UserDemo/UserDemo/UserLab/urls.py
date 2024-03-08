from django.urls import path

from UserDemo.UserLab import views

urlpatterns = [
    path('page', views.page, name='page'),
    path('loginpage', views.loginpage, name='login page'),
    path('registerpage', views.RegisterForm.as_view(), name='register page'),
    path('profile', views.profile, name='profile')
]
