
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Team, Activity, Leaderboard, Workout

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username', 'email']

class TeamSerializer(serializers.ModelSerializer):
	class Meta:
		model = Team
		fields = ['id', 'name']

class ActivitySerializer(serializers.ModelSerializer):
	class Meta:
		model = Activity
		fields = ['id', 'user', 'team', 'type', 'duration']

class LeaderboardSerializer(serializers.ModelSerializer):
	class Meta:
		model = Leaderboard
		fields = ['id', 'team', 'points']

class WorkoutSerializer(serializers.ModelSerializer):
	class Meta:
		model = Workout
		fields = ['id', 'name', 'description']
