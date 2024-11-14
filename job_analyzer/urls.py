# job_analyzer/urls.py
from django.contrib import admin
from django.urls import path, include
from analyzer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.analyze_description, name='home'),  # Redirect root URL to analyze_description view
    path('analyze/', include('analyzer.urls')),  # Include URLs from the analyzer app
]
