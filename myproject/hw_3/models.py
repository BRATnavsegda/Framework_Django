from django.db import models
from django.db.models import Manager


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date_reg = models.DateField(auto_now_add=True)
    orders = models.ManyToManyField('Order')

    objects = Manager()

    def __str__(self):
        return f'Name: {self.name}, ' \
               f'email: {self.email}, ' \
               f'phone: {self.phone}, ' \
               f'address: {self.address}, ' \
               f'date_reg: {self.date_reg} '


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    date_add = models.DateField(auto_now_add=True)

    objects = Manager()

    def __str__(self):
        return f'Name: {self.name}, ' \
               f'description: {self.description}, ' \
               f'price: {self.price}, ' \
               f'quantity: {self.quantity}, ' \
               f'date_add: {self.date_add} '


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_order = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Client: {self.customer}, ' \
               f'products: {self.products}, ' \
               f'total_price: {self.total_price}, ' \
               f'date_order: {self.date_order}'


