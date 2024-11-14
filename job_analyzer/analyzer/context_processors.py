# analyzer/context_processors.py

from .models import VisitorCount

def visitor_count(request):
    visitor_count = VisitorCount.objects.first()
    return {
        'visitor_count': visitor_count.count if visitor_count else 0
    }
