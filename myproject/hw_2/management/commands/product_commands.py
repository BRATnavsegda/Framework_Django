import decimal

from django.core.management import BaseCommand

from hw_2.models import Product


class CreateProductCommand(BaseCommand):
    help = "Create product."

    def handle(self, *args, **kwargs):
        product = Product(name='Product', description='Description', price=100, quantity=100)
        product.save()
        self.stdout.write(f'{product}')


class ReadProductCommand(BaseCommand):
    help = "Read product by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.filter(pk=pk).first()
        self.stdout.write(f'{product}')


class UpdateProductPriceCommand(BaseCommand):
    help = "Update product price by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')
        parser.add_argument('price', type=decimal.Decimal, help='Product new price')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        price = kwargs.get('price')
        product = Product.objects.filter(pk=pk).first()
        product.price = price
        product.save()
        self.stdout.write(f'{product}')


class DeleteProductCommand(BaseCommand):
    help = "Delete product by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.filter(pk=pk).first()
        if product is not None:
            product.delete()
        self.stdout.write(f'{product}')


