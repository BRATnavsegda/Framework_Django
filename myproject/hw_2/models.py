from django.db import models
from django.db.models import Manager

# Задание
# Создайте три модели Django: клиент, товар и заказ.
#
# Клиент может иметь несколько заказов. Заказ может содержать несколько товаров. Товар может входить в несколько
# заказов.
#
# Поля модели «Клиент»:
# — имя клиента
# — электронная почта клиента
# — номер телефона клиента
# — адрес клиента
# — дата регистрации клиента
#
# Поля модели «Товар»:
# — название товара
# — описание товара
# — цена товара
# — количество товара
# — дата добавления товара
#
# Поля модели «Заказ»:
# — связь с моделью «Клиент», указывает на клиента, сделавшего заказ
# — связь с моделью «Товар», указывает на товары, входящие в заказ
# — общая сумма заказа
# — дата оформления заказа.
#
# Допишите несколько функций CRUD для работы с моделями по желанию. Что по вашему мнению актуально в такой базе


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
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_order = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Client: {self.client}, ' \
               f'products: {self.products}, ' \
               f'total_price: {self.total_price}, ' \
               f'date_order: {self.date_order}'

