from django import forms

from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


# class AccountForm(forms.ModelForm):
#     class Meta:
#         model = AccountModel
#         fields = ['email', 'password', 'age']
#
#     password = forms.CharField(
#         widget=forms.PasswordInput()
#     )


class AccountUserCreationForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = (UserModel.USERNAME_FIELD,)
