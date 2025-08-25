# AUGUST 25
# SAMIP REGMI

from django.db import models
from django.contrib.auth.models import User



class Event(models.Model):
    # LEFT IS IN DB, RIGHT IS IN UI

    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    name = models.CharField(max_length=100, blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    location = models.CharField(max_length=150, default="Biratnagar International College")
    description = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    organized_by = models.CharField(max_length=100, default="BIC Devsphere")
    event_starting_date_time = models.DateTimeField(blank=False, null=False)
    event_ending_date_time = models.DateTimeField(blank=False, null=False)
    banner_image = models.ImageField(upload_to='event_banners/', blank=True, null=True)
    event_images = models.ImageField(upload_to='event_images/', blank=True, null=True)
    event_guest_speaker = models.CharField(max_length=100, blank=True, null=True)
    event_guest_speaker_image = models.ImageField(upload_to='guest_speakers/', blank=True, null=True)
    event_guest_speaker_bio = models.TextField(blank=True, null=True)
    registration_link = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='upcoming')


class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='event_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    

class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="registrations")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_registrations")
    registered_at = models.DateTimeField(auto_now_add=True)

