from django.core.management.base import BaseCommand
from analyzer.models import WordCount, CustomStopWord
from django.db.models import Q

class Command(BaseCommand):
    help = 'Delete stopwords from the WordCount database'

    def handle(self, *args, **kwargs):
        # Retrieve all custom stopwords
        custom_stop_words = CustomStopWord.objects.values_list('word', flat=True)
        all_stop_words = set(custom_stop_words)

        # Delete all entries in WordCount that match the stopwords
        deleted_count, _ = WordCount.objects.filter(word__in=all_stop_words).delete()

        # Print the result
        self.stdout.write(self.style.SUCCESS(f'Successfully deleted {deleted_count} stopword entries from WordCount.'))
