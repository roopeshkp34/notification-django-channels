import json
from channels.generic.websocket import AsyncWebsocketConsumer


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("conncted")
        self.room_name = self.scope["url_route"]["kwargs"]["id"]
        self.room_group_name = f"chat_{self.room_name}"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        print("Disconnected")
        self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        return super().disconnect(code)

    async def send_notification(self, event):
        notification = event["notification"]
        await self.send(text_data=json.dumps({"message": notification}))