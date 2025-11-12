from venv import create
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product,Cart,Customer
from django.contrib.auth.mixins import LoginRequiredMixin



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
    fields = ["category","name","description","price","image"]
    template_name = "store/product_form.html"
    success_url = reverse_lazy("product_list")

class ProductUpdateView(UpdateView):
    model = Product
    fields = ["category", "name", "description", "price", "image"]
    template_name = "store/product_list.html"
    success_url = reverse_lazy("product_list")

class ProductDeleteView(DeleteView):
    model = Product
    template_name ="store/delete_product.html"
    success_url = reverse_lazy("product_list")


class CArtDetailView(LoginRequiredMixin,DetailView):
    model = Cart
    template_name = "store/cart_detail.html"
    context_object_name = "cart"

    def get_object(self):
        customer=Customer.objects.get(user=self.request.user)
        cart,created=Cart.objects.get_or_create(customer=customer)
        return cart

    