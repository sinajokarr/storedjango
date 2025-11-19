from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
    FormView,         
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages  

from .models import Product, Cart, Customer, Category
from .forms import ContactForm       


class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class ProductListView(ListView):
    model = Product
    template_name = "store/product_list.html"
    context_object_name = "products"
    paginate_by = 12

    def get_queryset(self):
        queryset = (
            super()
            .get_queryset()
            .select_related("category")
            .order_by("-created_at")
        )
        category_slug = self.request.GET.get("category")
        search_query = self.request.GET.get("q")

        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)

        if search_query:
            queryset = queryset.filter(name__icontains=search_query)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all().order_by("name")
        context["current_category"] = self.request.GET.get("category") or ""
        context["search_query"] = self.request.GET.get("q") or ""
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "store/product_detail.html"
    context_object_name = "product"

    def get_queryset(self):
        return super().get_queryset().select_related("category")


class ProductCreateView(StaffRequiredMixin, CreateView):
    model = Product
    fields = ["category", "name", "description", "price", "image"]
    template_name = "store/product_form.html"
    success_url = reverse_lazy("store:products_list")


class ProductUpdateView(StaffRequiredMixin, UpdateView):
    model = Product
    fields = ["category", "name", "description", "price", "image"]
    template_name = "store/product_form.html"
    success_url = reverse_lazy("store:products_list")


class ProductDeleteView(StaffRequiredMixin, DeleteView):
    model = Product
    template_name = "store/delete_product.html"
    success_url = reverse_lazy("store:products_list")


class CartDetailView(LoginRequiredMixin, DetailView):
    model = Cart
    template_name = "store/cart_detail.html"
    context_object_name = "cart"

    def get_object(self):
        customer, _ = Customer.objects.get_or_create(user=self.request.user)
        cart, _ = Cart.objects.select_related("customer").get_or_create(
            customer=customer
        )
        return cart


class AboutView(TemplateView):
    template_name = "store/about.html"



class ContactView(FormView):
    template_name = "store/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("store:contact")

    def form_valid(self, form):

        messages.success(
            self.request,
            "Your message has been sent. Our team will reply within one business day.",
        )
        return super().form_valid(form)
