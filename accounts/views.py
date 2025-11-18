from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login
from .forms import CustomUserCreationForm

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("store:product_list")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
