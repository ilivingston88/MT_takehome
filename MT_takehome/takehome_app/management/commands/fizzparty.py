#https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/
from django.core.management.base import BaseCommand, CommandError
from takehome_app.models import FizzBuzz


class Command(BaseCommand):
    help = "get the FizzBuzz party started"

    def handle(self):
        for i in range(100):
            FizzBuzz.objects.create(
                useragent = 'fizzparty',
                message = 'this is FizzBuzz {i} from the FizzParty'
            )

        self.stdout.write(
                    self.style.SUCCESS('100 FizzBuzzes have entered the room')
                )       