from django.core.management import BaseCommand

from hw_2.models import Client


class CreateClientCommand(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):

        client = Client(name='John', email='john@example.com', phone='123456789', address='Moscow')
        client.save()
        self.stdout.write(f'{client}')


class ReadClientCommand(BaseCommand):
    help = "Read client by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()
        self.stdout.write(f'{client}')


class UpdateClientNameCommand(BaseCommand):
    help = "Update client name by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('name', type=str, help='Client name')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        client = Client.objects.filter(pk=pk).first()
        client.name = name
        client.save()
        self.stdout.write(f'{client}')


class DeleteClientCommand(BaseCommand):
    help = "Delete client by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()
        if client is not None:
            client.delete()
        self.stdout.write(f'{client}')
