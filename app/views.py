from django.http import JsonResponse
from django.shortcuts import render
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# Create your views here.

def index(request):
    return render(request, "index.html")

def send_notification(request):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "chat_1",
        {
            "type": "send_notification",
            "notification": "Done"
        }
    )

    return JsonResponse({"success": True})
