from django.db import models

# Create your models here.
# tasks/models.py

from django.utils import timezone

class Task(models.Model):
    CATEGORY_CHOICES = (
        ('Work', 'Work'),
        ('Study', 'Study'),
        ('Personal', 'Personal'),
    )

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    create_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
