from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Match

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user=User.objects.create_user(**validated_data)
        return user

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Match
        fields=['id','team1','team2','score_team1','score_team2','start_time','end_time','is_live']
        