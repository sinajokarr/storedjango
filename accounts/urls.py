from django.contrib.auth.views import LoginView
from django.urls import path

urlpatterns = [
    path( "accounts/login/",LoginView.as_view(template_name="account/login.html"),name="login",
    ),
]
