# analyzer/views.py

from django.shortcuts import render, redirect
from django.utils import timezone
from django.db.models import Sum
from django.core.paginator import Paginator
from datetime import timedelta
from collections import Counter
import re

from .forms import JobDescriptionForm, StopWordsForm
from .models import JobDescription, WordCount, CustomStopWord
from .utils import get_stop_words


# Analyze job description and save word counts
def analyze_description(request):
    if request.method == 'POST':
        form = JobDescriptionForm(request.POST)
        if form.is_valid():
            job_desc = form.save()
            words = re.findall(r'\b\w+\b', job_desc.text.lower())
            word_counts = Counter(words)
            
            # Save job description word counts
            for word, count in word_counts.items():
                WordCount.objects.create(job_description=job_desc, word=word, count=count)
            
            # Store resume_text in session only for comparison purposes
            resume_text = request.POST.get('resume_text', '').lower()
            request.session['resume_text'] = resume_text
            
            return redirect('results', job_desc_id=job_desc.id)
    else:
        form = JobDescriptionForm()
    return render(request, 'analyzer/analyze.html', {'form': form})



# Display word counts for an individual job description, excluding stop words
from django.http import HttpResponseRedirect

from django.http import HttpResponseRedirect

from django.http import HttpResponseRedirect
from django.db.models import Sum
import re
from collections import Counter

def view_results(request, job_desc_id):
    job_desc = JobDescription.objects.get(id=job_desc_id)
    all_stop_words = get_stop_words()

    # Get word counts from the job description, excluding stop words
    word_counts = (
        WordCount.objects
        .filter(job_description=job_desc)
        .exclude(word__in=all_stop_words)
        .order_by('-count')
    )

    # Retrieve resume_text from session for comparison only
    resume_text = request.session.get('resume_text', '').lower()

    # Extract words from resume text and filter out stop words
    resume_words = set(re.findall(r'\b\w+\b', resume_text))
    filtered_resume_words = resume_words - set(all_stop_words)

    # Determine matching and missing words
    job_words = set(word_counts.values_list('word', flat=True))
    matching_words = job_words & filtered_resume_words
    missing_words = job_words - matching_words

    # Fetch top words across all job descriptions, excluding stop words and limiting to top 5
    top_words = (
        WordCount.objects
        .exclude(word__in=all_stop_words)
        .values('word')
        .annotate(total_count=Sum('count'))
        .order_by('-total_count')[:5]
    )

    if request.method == "POST":
        selected_words = request.POST.getlist("selected_words")
        for word in selected_words:
            CustomStopWord.objects.get_or_create(word=word.lower())
        return HttpResponseRedirect(request.path_info)

    context = {
        'word_counts': word_counts,
        'job_desc': job_desc,
        'matching_words': matching_words,
        'missing_words': missing_words,
        'top_words': top_words,
    }

    return render(request, 'analyzer/results.html', context)





# Display the top words across all descriptions from the last 6 months
def top_words_view(request):
    six_months_ago = timezone.now() - timedelta(days=180)
    current_time = timezone.now()

    # Count job descriptions scanned in the last 6 months
    job_desc_count = JobDescription.objects.filter(created_at__gte=six_months_ago).count()

    # Handle POST request for stop word removal
    if request.method == 'POST' and 'delete_stop_words' in request.POST:
        CustomStopWord.objects.all().delete()
        return HttpResponseRedirect(request.path_info)

    # Retrieve combined stop words
    all_stop_words = get_stop_words()

    # Get the frequency filter from the request or set a default
    frequency_filter = int(request.GET.get('frequency', 1))  # Default to 1 if not provided

    # Filter top words by frequency and excluding stop words
    top_words = (
        WordCount.objects
        .filter(job_description__created_at__gte=six_months_ago)
        .exclude(word__in=all_stop_words)
        .values('word')
        .annotate(total_count=Sum('count'))
        .filter(total_count__gte=frequency_filter)  # Apply frequency filter
        .order_by('-total_count')
    )

    # Set up pagination
    paginator = Paginator(top_words, 50)  # Show 50 words per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Total word count for all job descriptions
    total_word_count = WordCount.objects.count()

    context = {
        'page_obj': page_obj,
        'start_date': six_months_ago,
        'end_date': current_time,
        'total_word_count': total_word_count,
        'job_desc_count': job_desc_count,  # Pass job description count
        'frequency_filter': frequency_filter  # Pass the current filter value
    }

    return render(request, 'analyzer/top_words.html', context)


# Add custom stop words to the database
def add_stop_words(request):
    if request.method == 'POST':
        if 'delete_last_entry' in request.POST:
            # Delete the most recent entry in CustomStopWord, if it exists
            last_custom_word = CustomStopWord.objects.order_by('-id').first()
            if last_custom_word:
                last_custom_word.delete()
            
            # Delete the most recent entry in WordCount (top keywords), if it exists
            last_word_count = WordCount.objects.order_by('-id').first()
            if last_word_count:
                last_word_count.delete()

            return redirect('add_stop_words')  # Redirect back to the form page

        # Otherwise, process the form to add stop words
        form = StopWordsForm(request.POST)
        if form.is_valid():
            words = form.cleaned_data['words']
            
            # Use regex to find words, ignoring numbers and punctuation
            words_list = re.findall(r'\b[a-zA-Z]+\b', words.lower())
            
            for word in words_list:
                # Store each unique word, ignoring duplicates
                CustomStopWord.objects.get_or_create(word=word)
            
            return redirect('stop_words_success')
    else:
        form = StopWordsForm()

    return render(request, 'analyzer/add_stop_words.html', {'form': form})


# Success message for adding stop words
def stop_words_success(request):
    return render(request, 'analyzer/stop_words_success.html')
