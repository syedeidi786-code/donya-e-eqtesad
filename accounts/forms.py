from django import forms
from django.contrib.auth.models import User
from .models import Profile


class SignupForm(forms.Form):

    full_name = forms.CharField(
        max_length=100
    )

    username = forms.CharField(
        max_length=100
    )

    email = forms.EmailField()

    phone = forms.CharField(
        max_length=15
    )

    password = forms.CharField(
        widget=forms.PasswordInput
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput
    )


    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm_password")

        if password != confirm:
            raise forms.ValidationError(
                "Passwords do not match"
            )

        return cleaned_data