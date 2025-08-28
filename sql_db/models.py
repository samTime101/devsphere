# AUGUST 25
# SAMIP REGMI
from django.db import models
from django.contrib.auth.models import AbstractUser

def event_banner_path(instance, filename):
    ext = filename.split('.')[-1]
    return f'event_{instance.id}/banner/event_{instance.id}_banner.{ext}'

def event_guest_speaker_path(instance, filename):
    ext = filename.split('.')[-1]
    return f'event_{instance.id}/guest_speaker/event_{instance.id}_guest_speaker.{ext}'

def event_image_path(instance, filename):
    return f'event_{instance.event.id}/images/event_{instance.event.id}_image_{filename}'

def blog_image_path(instance, filename):
    ext = filename.split('.')[-1]
    return f'blog_{instance.id}/images/blog_{instance.id}_image.{ext}'

# CUSTOM USER MODEL 
# STREAM RA SECTION
class User(AbstractUser):
    STREAM_CHOICES = [
        ('CS', 'CS'),
    ]
    SECTION_CHOICES = [
        ('L4CG1', 'L4CG1'),
        ('L4CG2', 'L4CG2'),
        ('L4CG3', 'L4CG3'),
        ('L4CG4', 'L4CG4'),
    ]
    stream = models.CharField(max_length=100, blank=True, null=True, choices=STREAM_CHOICES)
    section = models.CharField(max_length=50, blank=True, null=True, choices=SECTION_CHOICES)

class Event(models.Model):
    STATUS_CHOICES = [
        ('upcoming', 'upcoming'),
        ('ongoing', 'ongoing'),
        ('completed', 'completed'),
        ('cancelled', 'cancelled'),
    ]

    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=150, default="Biratnagar International College")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    organized_by = models.CharField(max_length=100, default="BIC Devsphere")
    event_starting_date_time = models.DateTimeField()
    event_ending_date_time = models.DateTimeField()
    banner_image = models.ImageField(upload_to=event_banner_path, blank=True, null=True)
    event_guest_speaker = models.CharField(max_length=100, blank=True, null=True)
    event_guest_speaker_image = models.ImageField(upload_to=event_guest_speaker_path, blank=True, null=True)
    event_guest_speaker_bio = models.TextField(blank=True, null=True)
    registration_link = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='upcoming')

class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=event_image_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class BlogImage(models.Model):
    blog = models.ForeignKey('Blogs', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=blog_image_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="registrations")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_registrations")
    registered_at = models.DateTimeField(auto_now_add=True)

class Blogs(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=blog_image_path, blank=True, null=True)
    approved = models.BooleanField(default=False)


class DiscordMember(models.Model):
    discord_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    global_name = models.CharField(max_length=100, blank=True, null=True)
    discriminator = models.CharField(max_length=10)
    joined_at = models.DateTimeField(null=True)
    roles = models.TextField(blank=True)
    avatar_url = models.URLField(blank=True, null=True)


# FORUM AND THREAD KO LAGI
class Forum(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='forums')

class Question(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='questions')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')

class Comment(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

class Vote(models.Model):
    VOTE_CHOICES = [
        (1, 'Upvote'),
        (-1, 'Downvote'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='votes')
    value = models.SmallIntegerField(choices=VOTE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # A USER CAN HAVE ONLY ONE VOTE PER ANSWER
        unique_together = ('user', 'answer')