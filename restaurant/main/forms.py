from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'customer_email', 'product_name', 'quantity']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-input'}),
            'customer_email': forms.EmailInput(attrs={'class': 'form-input'}),
            'product_name': forms.TextInput(attrs={'class': 'form-input'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-input', 'min': 1}),
        }