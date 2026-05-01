from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import UserProfile, Team, Activity, Leaderboard
from .serializers import UserSerializer, UserProfileSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileSerializer

class TeamViewSet(viewsets.ModelViewSet):
	queryset = Team.objects.all()
	serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
	queryset = Activity.objects.all()
	serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
	queryset = Leaderboard.objects.all()
	serializer_class = LeaderboardSerializer
