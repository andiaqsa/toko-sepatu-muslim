from django.db import models

# Create your models here.
class MoodEntry(models.Model):
    Name = models.CharField(max_length=255)
    Price = models.IntegerField()
    Description = models.TextField()


