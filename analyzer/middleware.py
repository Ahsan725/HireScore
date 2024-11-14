# analyzer/middleware.py

from .models import VisitorCount

class VisitorCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Increment the visitor count on each page load
        if not request.session.get('counted'):
            visitor_count, created = VisitorCount.objects.get_or_create(id=1)
            visitor_count.count += 1
            visitor_count.save()
            request.session['counted'] = True  # Set session to avoid multiple increments in one session

        response = self.get_response(request)
        return response
