from django.db import models
from django.utils import timezone
from django.conf import settings


class Region(models.Model):
    name = models.CharField(max_length=200, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Event(models.Model):

    name = models.CharField(max_length=200)
    event_name = models.CharField(max_length=200)
    event_date = models.DateTimeField('date published') #datefield
    location = models.CharField(max_length=200)
    start_time = models.TimeField
    end_time = models.TimeField
    event_desr = models.CharField(max_length=200)
    event_guest_count = models.IntegerField
    event_host_count = models.IntegerField
    event_dangerous_equipment = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    region = models.ForeignKey(Region, related_name='region', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.event_name
