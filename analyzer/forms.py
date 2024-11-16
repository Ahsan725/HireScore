# analyzer/forms.py

from django import forms
from .models import JobDescription

class JobDescriptionForm(forms.ModelForm):
    resume_text = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'rows': 6, 
            'placeholder': 'Paste the resume text here...'
        }),
        required=False,
        label="Paste Your Resume Text"
    )

    class Meta:
        model = JobDescription
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 6,
                'placeholder': 'Paste the job description here...'
            }),
        }


class StopWordsForm(forms.Form):
    words = forms.CharField(
        label="Words to Exclude",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter words separated by commas'
        })
    )
