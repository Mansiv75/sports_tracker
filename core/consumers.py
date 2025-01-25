import json
from channels.generic.websocket import AsyncWebsocketConsumer

class MatchConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.match_id=self.scope['url_route']['kwargs']['match_id']
        self.match_group_name=f"match_{self.match_id}"

        await self.channel_layer.group_add(
            self.match_group_name,
            self.channel_name,
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.match_group_name,
            self.channel_name,
        )
    
    async def receive(self, text_data):
        data=json.loads(text_data)
        score_team1=data['score_team1']
        score_team2=data['score_team2']

        await self.channel_layer.group_send(
            self.match_group_name,
            {
                'type': 'score_update',
                'score_team1': score_team1,
                'score_team2': score_team2,
            },
        )

    async def score_update(self, event):
        await self.send(text_data=json.dumps({
            'score_team1': event['score_team1'],
            'score_team2': event['score_team2'],
        }))