# Задание №6
# Доработаем задачу про клиентов, заказы и товары из
# прошлого семинара.
# Создайте форму для редактирования товаров в базе
# данных.
from django import forms

from .models import Product, Order, Client


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity']


class AddOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'products', 'total_price']


class AddClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'address']


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }