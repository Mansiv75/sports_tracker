from django.urls import path
from .views import RegisterView, MatchListView, MatchCreateView, MatchScoreUpdateView, MatchCompleteView, LeaderboardView
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', ObtainAuthToken.as_view(), name='login'),
    path('matches/', MatchListView.as_view(), name='matches-list'),
    path('matches/create/', MatchCreateView.as_view(), name='matches-create'),
    path('matches/<int:pk>/complete/', MatchCompleteView.as_view(), name='matches-complete'),
    path('leaderboard/', LeaderboardView.as_view(), name='leaderboard'),
]