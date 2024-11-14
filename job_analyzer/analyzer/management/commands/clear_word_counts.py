from django.core.management.base import BaseCommand
from analyzer.models import WordCount
from django.db.models import Q

class Command(BaseCommand):
    help = 'Deletes all WordCount records'

    def handle(self, *args, **kwargs):
        WordCount.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all WordCount records'))
