from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Кастомная команда для создания суперпользователя"""

    def handle(self, *args, **kwargs):
        user = User.objects.create(email='admin@sky.pro',
                                   first_name='Artem',
                                   last_name='Matrashov',
                                   is_staff=True,
                                   is_superuser=True)

        user.set_password('admin')
        user.save()