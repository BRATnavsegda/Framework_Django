from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView

from .forms import AddClientForm, ProductUpdateForm
from .models import Client, Product


class AddClient(CreateView):
    model = Client
    template_name = 'hw_4/client_form.html'
    form_class = AddClientForm


class ClientPage(DetailView):
    model = Client
    template_name = 'hw_4/client_page.html'


class UpdateProductView(UpdateView):
    model = Product
    template_name = 'hw_4/update_product.html'
    form_class = ProductUpdateForm


class ProductView(DetailView):
    model = Product
    template_name = 'hw_4/product_page.html'
