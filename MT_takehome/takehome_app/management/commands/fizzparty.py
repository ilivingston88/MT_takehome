#https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/
from django.core.management.base import BaseCommand, CommandError
from takehome_app.models import FizzBuzz


class Command(BaseCommand):
    #message - what does this command do
    help = "get the FizzBuzz party started"
    #args/kwargs are required here? operation doesn't error
    #but fails to populate without those arguments
    def handle(self, *args, **kwargs):
        #how many fizzbuzzes to create
        for i in range(100):
            FizzBuzz.objects.create(
                #id and date generated automatically
                useragent = 'fizzparty',
                #'f' before message indicates f-string (allows expressions inside strings)
                message = f'this is FizzBuzz {i} from the FizzParty'
            )
        #message that appears in command line if/when successfull
        self.stdout.write(
                    self.style.SUCCESS('100 FizzBuzzes have entered the room')
                )       