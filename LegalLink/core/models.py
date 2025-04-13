from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES,default='other')
    city = models.CharField(max_length=100,blank=True)
    state = models.CharField(max_length=100, blank=True)
    is_helper = models.BooleanField(default=False)
    contact_info = models.TextField(blank=True)
    karma = models.IntegerField(default=0)  # Helping points for a good helper
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return self.user.username


class Case(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('closed', 'Closed'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    full_description = models.TextField()
    charges = models.JSONField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")
    created_at = models.DateTimeField(auto_now_add=True)
    lawyers = models.ManyToManyField('Lawyer', blank=True)  # New field for associated lawyers.

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class CaseEvent(models.Model):
    EVENT_TYPES = (
        ('first_hearing', 'First Hearing'),
        ('next_hearing', 'Next Hearing'),
        ('verdict', 'Verdict'),
    )

    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='events')
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    date = models.DateField()
    notes = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.event_type} - {self.case.title}"

    class Meta:
        ordering = ['date']


class Lawyer(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    contact_info = models.TextField()
    linked_case = models.ForeignKey(Case, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    
class UserUpvote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="given_upvotes")
    voted = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_upvotes")
    
    class Meta:
        unique_together = (('voter', 'voted'),)
        
    def __str__(self):
        return f"{self.voter.username} upvoted {self.voted.username}"