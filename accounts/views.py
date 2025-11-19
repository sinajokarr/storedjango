from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("store:products_list")

    def form_valid(self, form):
        user = form.save()
        # auto login
        from django.contrib.auth import login
        login(self.request, user)
        return super().form_valid(form)


def custom_logout(request):
    """
    Simple logout view:
    - logs the user out
    - renders logged_out.html with status 200
    """
    logout(request)
    return render(request, "registration/logged_out.html")
