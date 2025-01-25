from django.urls import path
from .views import RegisterView, MatchListView, MatchCreateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('matches/', MatchListView.as_view(), name='matches-list'),
    path('matches/create/', MatchCreateView.as_view(), name='matches-create'),
]