from django.core.management import BaseCommand

from lecture_2.models import User


class Command(BaseCommand):
    help = "Get all users."

    def handle(self, *args, **kwargs):
        users = User.objects.all()

        self.stdout.write(f'{users}')
        