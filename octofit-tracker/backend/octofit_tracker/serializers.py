from rest_framework import serializers
from .models import User, Team, Activity, Workout, Leaderboard

class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined', 'is_active']

class TeamSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    members = UserSerializer(many=True, read_only=True)
    member_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.all(),
        source='members',
        write_only=True
    )

    class Meta:
        model = Team
        fields = ['id', 'name', 'members', 'member_ids', 'created_at']

class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='user',
        write_only=True
    )

    class Meta:
        model = Activity
        fields = ['id', 'user', 'user_id', 'type', 'duration', 'calories', 'date']

class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    suggested_for = UserSerializer(many=True, read_only=True)
    suggested_for_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.all(),
        source='suggested_for',
        write_only=True
    )

    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'suggested_for', 'suggested_for_ids']

class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    team = TeamSerializer(read_only=True)
    team_id = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(),
        source='team',
        write_only=True
    )

    class Meta:
        model = Leaderboard
        fields = ['id', 'team', 'team_id', 'total_points']
