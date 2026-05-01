from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from octofit_tracker.api.models import UserProfile, Team, Activity, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        UserProfile.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()

        # Create Marvel users
        marvel_users = [
            {'username': 'ironman', 'email': 'ironman@marvel.com', 'first_name': 'Tony', 'last_name': 'Stark'},
            {'username': 'captainamerica', 'email': 'cap@marvel.com', 'first_name': 'Steve', 'last_name': 'Rogers'},
            {'username': 'spiderman', 'email': 'spidey@marvel.com', 'first_name': 'Peter', 'last_name': 'Parker'},
        ]
        marvel_team = Team.objects.create(name='Team Marvel', description='Earth’s Mightiest Heroes', creator=None)
        marvel_team_members = []
        for user_data in marvel_users:
            user = User.objects.create_user(**user_data, password='password')
            marvel_team_members.append(user)
            UserProfile.objects.create(user=user, bio=f"{user.first_name} {user.last_name} is a Marvel hero.", fitness_level='ADVANCED')
        marvel_team.creator = marvel_team_members[0]
        marvel_team.save()
        marvel_team.members.set(marvel_team_members)

        # Create DC users
        dc_users = [
            {'username': 'batman', 'email': 'batman@dc.com', 'first_name': 'Bruce', 'last_name': 'Wayne'},
            {'username': 'superman', 'email': 'superman@dc.com', 'first_name': 'Clark', 'last_name': 'Kent'},
            {'username': 'wonderwoman', 'email': 'wonderwoman@dc.com', 'first_name': 'Diana', 'last_name': 'Prince'},
        ]
        dc_team = Team.objects.create(name='Team DC', description='Justice League', creator=None)
        dc_team_members = []
        for user_data in dc_users:
            user = User.objects.create_user(**user_data, password='password')
            dc_team_members.append(user)
            UserProfile.objects.create(user=user, bio=f"{user.first_name} {user.last_name} is a DC hero.", fitness_level='ADVANCED')
        dc_team.creator = dc_team_members[0]
        dc_team.save()
        dc_team.members.set(dc_team_members)

        # Add activities for all users
        all_users = marvel_team_members + dc_team_members
        for user in all_users:
            Activity.objects.create(
                user=user,
                activity_type='RUNNING',
                duration_minutes=30,
                calories_burned=300,
                distance_km=5.0,
                notes=f"{user.username} ran 5km.",
                activity_date=timezone.now().date()
            )
            Activity.objects.create(
                user=user,
                activity_type='CYCLING',
                duration_minutes=60,
                calories_burned=600,
                distance_km=20.0,
                notes=f"{user.username} cycled 20km.",
                activity_date=timezone.now().date()
            )
            # Leaderboard
            Leaderboard.objects.create(
                user=user,
                total_activities=2,
                total_calories=900,
                total_distance=25.0,
                rank=None
            )
        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
