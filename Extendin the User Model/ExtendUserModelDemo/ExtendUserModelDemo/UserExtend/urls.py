from django.urls import path

from ExtendUserModelDemo.UserExtend import views
from ExtendUserModelDemo.UserExtend.views import CreateUser, LoginUser

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', CreateUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login')
]