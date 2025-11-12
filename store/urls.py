from sys import path_hooks

from django.urls import path
from .views import ProductCreateView, ProductDetailView, ProductUpdateView, ProductListView, ProductDeleteView,CArtDetailView

urlpatterns = [

    path("products/",ProductListView.as_view(),name="products_list"),
    path("products/<int:pk>",ProductDetailView.as_view(),name="products_detail"),
    path("products/new/",ProductCreateView.as_view(),name="products_create"),
    path("products/<int:pk>/edit/",ProductUpdateView.as_view(),name="products_update"),
    path("paroducts/<int:pk>/detail/",ProductDetailView.as_view(),name="products_detail"),
    path("product/<int:pk>/delete/",ProductDeleteView.as_view(),name="products_delete"),
    path("cart/",CArtDetailView.as_view(), name="cart_detail"),
]