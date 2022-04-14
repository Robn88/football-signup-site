from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_posts")
    event_date_and_time = models.DateTimeField()
    venue = models.CharField(max_length=100)
    max_participants = models.IntegerField()
    extra_info = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['event_date_and_time']

    def __str__(self):
        return self.title
    

class Registration(models.Model):

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="event_registration")
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    ball = models.BooleanField(default=False)
    bibs = models.BooleanField(default=False)
