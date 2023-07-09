from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=200)
#     password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(AuthenticationForm):
    pass

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # fields = UserCreationForm.Meta.fields + ("email", "first_name", "last_name")
        fields = UserCreationForm.Meta.fields + ("email",)
