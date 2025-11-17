from django.urls import path
from django.views.generic import RedirectView

from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    CartDetailView,
    AboutView,
    ContactView,
)

app_name = "store"

urlpatterns = [
    path(
        "",
        RedirectView.as_view(pattern_name="store:products_list", permanent=False),
        name="home",
    ),
    path("products/", ProductListView.as_view(), name="products_list"),
    path("products/new/", ProductCreateView.as_view(), name="products_create"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="products_detail"),
    path("products/<int:pk>/edit/", ProductUpdateView.as_view(), name="products_update"),
    path(
        "products/<int:pk>/delete/",
        ProductDeleteView.as_view(),
        name="products_delete",
    ),
    path("cart/", CartDetailView.as_view(), name="cart_detail"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ContactView.as_view(), name="contact"),
]
