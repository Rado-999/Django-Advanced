from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from UserModel.UserApp.models import UserProfile


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }


user_model = get_user_model()


class UserRegistrationForm2(UserCreationForm):
    class Meta:
        model = user_model
        fields = ('username','email','first_name')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

