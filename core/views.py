from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, MatchSerializer
from .models import Match
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from core.utils import update_leaderboard
class RegisterView(APIView):
    def post(self, request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#create match
class MatchCreateView(APIView):
    def post(self, request):
        serializer=MatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Get all matches
class MatchListView(APIView):
    def get(self, request):
        matches=Match.objects.all()
        serializer=MatchSerializer(matches, many=True)
        return Response(serializer.data)

class MatchScoreUpdateView(APIView):
    def post(self, request, pk):
        try:
            match=Match.objects.get(pk=pk)
            match.score_team1=request.data.get('score_team1', match.score_team1)
            match.score_team2=request.data.get('score_team2', match.score_team2)
            match.save()

            channel_layer=get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                f"match_{pk}",
                {
                    "type": "score_update",
                    "score_team1": match.score_team1,
                    "score_team2": match.score_team2,
                }
            )
            serializer=MatchSerializer(match)
            return Response(serializer.data)
        except Match.DoesNotExist:
            return Response({"error":"Match not found"},status=status.HTTP_404_NOT_FOUND)

class MatchCompleteView(APIView):
    def post(self, request, pk):
        try:
            match=Match.objects.get(pk=pk)
            match.is_completed=True
            match.save()

            if match.score_team1> match.score_team2:
                update_leaderboard(match.team1, 3)
                update_leaderboard(match.team2, 0)
            elif match.score_team1<match.score_team2:
                update_leaderboard(match.team1, 0)
                update_leaderboard(match.team2, 3)
            else:
                update_leaderboard(match.team1, 1)
                update_leaderboard(match.team2, 1)
            return Response({"message":"Match completed, Leaderboard updated successfully"})
        
        except Match.DoesNotExist:
            return Response({"error":"Match not found"},status=status.HTTP_404_NOT_FOUND)

class LeaderboardView(APIView):
    def get(self, request):
        top_teams=get_top_teams()
        return Response(top_teams)
