from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, UserProfileViewSet, TeamViewSet, ActivityViewSet, LeaderboardViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'userprofiles', UserProfileViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'leaderboard', LeaderboardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
