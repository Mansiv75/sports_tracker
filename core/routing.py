from django.urls import path 
from .consumers import MatchConsumer

websocket_urlpatterns = [
    path('ws/match/<int:match_id>/', MatchConsumer.as_asgi()),
]