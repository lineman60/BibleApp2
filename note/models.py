from django.db import models

# Create your models here.
class Note(models.Model):
    content = models.TextField()
    bible_book = models.CharField(max_length=3)
    bible_chapter = models.IntegerField()
    bible_verse = models.IntegerField()
    source = models.CharField(max_length=200)
