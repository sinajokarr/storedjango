from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product, Cart, Customer

class ProductListView(ListView):
    model = Product
    template_name = "store/product_list.html"
    context_object_name = "products"

class ProductDetailView(DetailView):
    model = Product
    template_name = "store/product_detail.html"
    context_object_name = "product"

class ProductCreateView(CreateView):
    model = Product
    fields = ["category", "name", "description", "price", "image"]
    template_name = "store/product_form.html"
    success_url = reverse_lazy("store:products_list")

class ProductUpdateView(UpdateView):
    model = Product
    fields = ["category", "name", "description", "price", "image"]
    template_name = "store/product_form.html"
    success_url = reverse_lazy("store:products_list")

class ProductDeleteView(DeleteView):
    model = Product
    template_name = "store/delete_product.html"
    success_url = reverse_lazy("store:products_list")

class CartDetailView(LoginRequiredMixin, DetailView):
    model = Cart
    template_name = "store/cart_detail.html"
    context_object_name = "cart"

    def get_object(self):
        customer, _ = Customer.objects.get_or_create(user=self.request.user)
        cart, _ = Cart.objects.get_or_create(customer=customer)
        return cart

class AboutView(TemplateView):
    template_name = "store/about.html"
    
class ContactView(TemplateView):
    template_name = "store/contact.html"