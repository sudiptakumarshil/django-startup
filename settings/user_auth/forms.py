from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms


class RegisterForm(UserCreationForm):
    dob = forms.DateField(required=True)
    address = forms.CharField(max_length=255, required=False)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "dob",
            "password1",
            "password2",
            "address",
        ]
