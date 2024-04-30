from django.db import models
from django.utils import timezone


# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    event_date = models.DateTimeField()
    time_end = models.DateTimeField()
    address = models.CharField(max_length=100)
    registration_link = models.URLField(max_length=200)
    album_id = models.ForeignKey('Album', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def event_has_passed(self):
        return self.event_date < timezone.now()


class Album(models.Model):
    media_id = models.ForeignKey("Media", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title


class Media(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    
    def __str__(self):
        return self.name


class Official(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    POSITION_CHOICES = (
        ("P1", "Position 1"),
        ("P2", "Position 2"),
        ("P3", "Position 3"),
    )

    position = models.CharField(max_length=50, choices=POSITION_CHOICES)

    quote = models.CharField(max_length=100)
    social_id = models.ForeignKey("Social", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Social(models.Model):
    email = models.EmailField(max_length=200)
    website = models.URLField(max_length=200)
    github = models.URLField(max_length=200)
    discord = models.URLField(max_length=200)
    linkedid = models.URLField(max_length=200)
    
    official_id = models.ForeignKey('Official', on_delete=models.CASCADE)

    def __str__(self):
        return f'{Official_id} social media'


class Subscribers(models.Model):
    email = models.EmailField(max_length=200)
    created_at = timezone.now()
