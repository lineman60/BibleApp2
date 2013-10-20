from django.db import models

# Create your models here.
class Note(models.Model):
    content = models.TextField()
    bible_book = models.CharField(max_length=3)
    bible_chapter = models.CharField(max_length=3)
    bible_verse = models.CharField(max_length=3)
    source = models.CharField(max_length=200)
