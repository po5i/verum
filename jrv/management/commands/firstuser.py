from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):

        try:
            User.objects.get(id=1)
            self.stdout.write('First user already exists')
        except:
            user = User.objects.create(first_name="Super",last_name="Administrador",username="posi",email="carlos.po5i@gmail.com",is_staff=True,is_active=True,is_superuser=True)
            user.set_password('cambiame')
            user.save()

            self.stdout.write('Created first user (posi/cambiame)')
