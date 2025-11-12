from django.contrib import admin
from .models import Category, Product, Customer, Order, OrderItem, Cart, CartItem
from .forms import CategoryForm, ProductForm

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    list_display = ("name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ("name", "category", "price", "created_at", "updated_at")
    list_filter = ("category", "created_at")
    search_fields = ("name", "description")
    readonly_fields = ("created_at", "updated_at")
    list_per_page = 20

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("user", "phone", "address")
    search_fields = ("user__username", "user__email", "phone")

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("price", "quantity")

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "created_at", "paid", "get_total")
    list_filter = ("paid", "created_at")
    inlines = [OrderItemInline]

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("customer", "created_at")
    inlines = [CartItemInline]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "quantity", "price")
    search_fields = ("product__name",)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("cart", "product", "quantity")
    search_fields = ("product__name",)
