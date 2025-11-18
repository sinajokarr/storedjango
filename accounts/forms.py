from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email", "phone")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if CustomUser.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Plase Write a New Email ")
        return email

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "phone", "is_active")

class CustomAuthenticationForm(AuthenticationForm):
    pass
