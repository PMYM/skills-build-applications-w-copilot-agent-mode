from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Team, Activity, Leaderboard

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'bio', 'avatar', 'fitness_level', 'created_at', 'updated_at']

class TeamSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    members = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'creator', 'members', 'created_at', 'updated_at']

class ActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration_minutes', 'calories_burned', 'distance_km', 'notes', 'logged_at', 'activity_date']

class LeaderboardSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'total_activities', 'total_calories', 'total_distance', 'rank', 'updated_at']
