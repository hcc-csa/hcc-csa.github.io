from django.db import models
from django.utils import timezone


# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    event_date = models.DateTimeField()

    def __str__(self):
        return self.name

    def event_has_passed(self):
        return self.event_date < timezone.now()
