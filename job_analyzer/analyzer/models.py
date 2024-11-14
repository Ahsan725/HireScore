# analyzer/models.py

from django.db import models

class JobDescription(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically adds timestamp when record is created

    def __str__(self):
        return f"Job Description {self.id}"

class WordCount(models.Model):
    job_description = models.ForeignKey(JobDescription, on_delete=models.CASCADE)
    word = models.CharField(max_length=100)
    count = models.IntegerField()

    class Meta:
        unique_together = ('job_description', 'word')

# analyzer/models.py

from django.db import models

class CustomStopWord(models.Model):
    word = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.word
# analyzer/models.py

from django.db import models

class VisitorCount(models.Model):
    count = models.PositiveIntegerField(default=0)  # Field to store the count of visitors

    def __str__(self):
        return f"Visitor Count: {self.count}"
