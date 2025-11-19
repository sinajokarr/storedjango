from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm,
)
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        
        fields = ("username", "email", "phone")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

       
        for name in ("username", "email", "phone", "password1", "password2"):
            field = self.fields[name]
            existing = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = (existing + " auth-input").strip()

     
        self.fields["username"].widget.attrs.setdefault("placeholder", "Your username")
        self.fields["email"].widget.attrs.setdefault("placeholder", "you@example.com")
        self.fields["phone"].widget.attrs.setdefault("placeholder", "+90 5xx xxx xx xx")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email and CustomUser.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Please use a different email address.")
        return email


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "phone", "is_active")


class CustomAuthenticationForm(AuthenticationForm):
    """Login form with the same UI classes"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name in ("username", "password"):
            field = self.fields[name]
            existing = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = (existing + " auth-input").strip()
            

