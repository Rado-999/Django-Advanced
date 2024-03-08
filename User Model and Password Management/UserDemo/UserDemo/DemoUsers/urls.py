from django.urls import path

from UserDemo.DemoUsers import views
from UserDemo.DemoUsers.views import LoginUserView, RegisterView

urlpatterns = [
    path('', views.index, name='home'),
    path('auth', views.auth_user, name='auth_user'),
    # path('form', views.create_user_view, name= 'create_user'),
    path('register', RegisterView.as_view(), name='register_user'),
    # path('auth_form', Usser.as_view(), name = 'auth_user'),
    path('login', LoginUserView.as_view(), name='loginuser'),
    path('loged', views.login_with_next_parameter, name='login2')
]