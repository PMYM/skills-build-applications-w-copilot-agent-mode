from django.db import models
from django.contrib.auth.models import User

# User Profile Model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    avatar = models.URLField(blank=True, null=True)
    fitness_level = models.CharField(
        max_length=20,
        choices=[
            ('BEGINNER', 'Beginner'),
            ('INTERMEDIATE', 'Intermediate'),
            ('ADVANCED', 'Advanced'),
        ],
        default='BEGINNER'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


# Activity Model
class Activity(models.Model):
    ACTIVITY_TYPES = [
        ('RUNNING', 'Running'),
        ('WALKING', 'Walking'),
        ('CYCLING', 'Cycling'),
        ('SWIMMING', 'Swimming'),
        ('WEIGHT_TRAINING', 'Weight Training'),
        ('YOGA', 'Yoga'),
        ('OTHER', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    duration_minutes = models.IntegerField()  # Duration in minutes
    calories_burned = models.FloatField()
    distance_km = models.FloatField(null=True, blank=True)  # For distance-based activities
    notes = models.TextField(blank=True, null=True)
    logged_at = models.DateTimeField(auto_now_add=True)
    activity_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.activity_type} ({self.activity_date})"


# Team Model
class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_teams')
    members = models.ManyToManyField(User, related_name='teams')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Leaderboard Model (calculated views)
class Leaderboard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='leaderboard')
    total_activities = models.IntegerField(default=0)
    total_calories = models.FloatField(default=0.0)
    total_distance = models.FloatField(default=0.0)
    rank = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Leaderboard"

    class Meta:
        ordering = ['rank']

