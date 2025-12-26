
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Team, Activity, Leaderboard, Workout

class APIRootTests(APITestCase):
	def test_api_root(self):
		url = reverse('api-root')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

class UserTests(APITestCase):
	def test_list_users(self):
		User.objects.create_user(username='testuser', email='test@example.com', password='pass')
		url = reverse('user-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

class TeamTests(APITestCase):
	def test_list_teams(self):
		Team.objects.create(name='Test Team')
		url = reverse('team-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

class ActivityTests(APITestCase):
	def test_list_activities(self):
		user = User.objects.create_user(username='testuser2', email='test2@example.com', password='pass')
		team = Team.objects.create(name='Test Team 2')
		Activity.objects.create(user=user, team=team, type='run', duration=10)
		url = reverse('activity-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

class LeaderboardTests(APITestCase):
	def test_list_leaderboard(self):
		team = Team.objects.create(name='Test Team 3')
		Leaderboard.objects.create(team=team, points=100)
		url = reverse('leaderboard-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

class WorkoutTests(APITestCase):
	def test_list_workouts(self):
		Workout.objects.create(name='Test Workout', description='desc')
		url = reverse('workout-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
