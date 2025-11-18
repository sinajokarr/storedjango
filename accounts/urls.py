from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView

app_name = "accounts"

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(template_name="registration/password_change_form.html"),
        name="password_change",
    ),
    path(
        "password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(template_name="registration/password_change_done.html"),
        name="password_change_done",
    ),
]