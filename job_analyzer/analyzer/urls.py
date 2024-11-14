# analyzer/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('analyze/', views.analyze_description, name='analyze_description'),
    path('results/<int:job_desc_id>/', views.view_results, name='results'),
    path('top-words/', views.top_words_view, name='top_words'),
    path('add-stop-words/', views.add_stop_words, name='add_stop_words'),  # Add stop words page
    path('stop-words-success/', views.stop_words_success, name='stop_words_success'),  # Success page
]
