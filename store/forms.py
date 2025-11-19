from django import forms
from .models import Product, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "slug"]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["category", "name", "description", "price", "image"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4})
        }
class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=100, label="Full name")
    email = forms.EmailField(label="Email")
    topic = forms.CharField(max_length=100, label="Topic")
    budget = forms.CharField(
        max_length=100,
        label="Approx. budget (optional)",
        required=False,
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea,
    )