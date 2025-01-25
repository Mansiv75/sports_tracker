from django.urls import path
from .views import RegisterView, MatchListView, MatchCreateView, MatchScoreUpdateView, MatchCompleteView, LeaderboardView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('matches/', MatchListView.as_view(), name='matches-list'),
    path('matches/create/', MatchCreateView.as_view(), name='matches-create'),
    path('matches/<int:pk>/complete/', MatchCompleteView.as_view(), name='matches-complete'),
    path('leaderboard/', LeaderboardView.as_view(), name='leaderboard'),
]