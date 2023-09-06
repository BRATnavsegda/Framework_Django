
from django.core.management import BaseCommand

from hw_2.models import Order, Product


class CreateOrderCommand(BaseCommand):
    help = "Create order."

    def add_arguments(self, parser):
        parser.add_argument('client_pk', type=int, help='Client ID')
        parser.add_argument('products', type=int, nargs='+', help='Product IDs')

    def handle(self, *args, **kwargs):
        products = kwargs.get('products')
        client_id = kwargs.get('client_pk')
        all_prices = 0
        for product in products:
            all_prices += product.price
        order = Order(client=client_id, products=products, total_price=all_prices)
        order.save()
        self.stdout.write(f'{order}')


class ReadOrderCommand(BaseCommand):
    help = "Read order by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        order = Order.objects.filter(pk=pk).first()
        self.stdout.write(f'{order}')


class DeleteOrderCommand(BaseCommand):
    help = "Delete order by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        order = Order.objects.filter(pk=pk).first()
        if order is not None:
            order.delete()
        self.stdout.write(f'{order}')
