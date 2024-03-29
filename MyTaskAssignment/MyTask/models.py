from django.db import models

# Create your models here.

from django.utils import timezone

class Task(models.Model):
    CATEGORY_CHOICES = (
        ('Work', 'Work'),
        ('Study', 'Study'),
        ('Personal', 'Personal'),
    )

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    # Here create_time & updated_time will record the time automatic
    create_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
