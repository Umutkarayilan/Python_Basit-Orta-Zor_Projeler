 #   Proje Açıklaması: Django Channels kullanarak gerçek zamanlı sohbet uygulaması geliştirin.

# terminalde django projesi oluşturun ve channels ekleyin
# pip install channels

# settings.py
INSTALLED_APPS = [
    ...
    'channels',
    'chat',  # Kendi uygulamanız
]

ASGI_APPLICATION = 'proje_name.asgi.application'

# proje_name/asgi.py
import os
import django
from channels.routing import get_default_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proje_name.settings')
django.setup()
application = get_default_application()

# chat/models.py
from django.db import models
from django.contrib.auth.models import User

class Mesaj(models.Model):
    kullanici = models.ForeignKey(User, on_delete=models.CASCADE)
    mesaj = models.TextField()
    zaman = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.kullanici.username}: {self.mesaj}"

# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'genel_sohbet'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # WebSocket'ten gelen mesajı alır
    async def receive(self, text_data):
        data = json.loads(text_data)
        mesaj = data['mesaj']
        kullanici = data['kullanici']

        # Mesajı grup üyelerine gönderir
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'sohbet_mesaji',
                'mesaj': mesaj,
                'kullanici': kullanici,
            }
        )

    # Grup üyelerine mesaj gönderir
    async def sohbet_mesaji(self, event):
        mesaj = event['mesaj']
        kullanici = event['kullanici']

        await self.send(text_data=json.dumps({
            'mesaj': mesaj,
            'kullanici': kullanici,
        }))

# chat/routing.py
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/$', consumers.ChatConsumer.as_asgi()),
]

# proje_name/routing.py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})

# chat/templates/chat/index.html
<!DOCTYPE html>
<html>
<head>
    <title>Sohbet</title>
</head>
<body>
    <h1>Gerçek Zamanlı Sohbet</h1>
    <div id="sohbet"></div>
    <input type="text" id="kullanici" placeholder="Kullanıcı Adı">
    <input type="text" id="mesaj" placeholder="Mesaj">
    <button onclick="gonder()">Gönder</button>

    <script>
        var socket = new WebSocket('ws://' + window.location.host + '/ws/chat/');

        socket.onmessage = function(e) {
            var data = JSON.parse(e.data);
            var sohbet = document.getElementById('sohbet');
            sohbet.innerHTML += '<p><strong>' + data.kullanici + ':</strong> ' + data.mesaj + '</p>';
        };

        function gonder() {
            var kullanici = document.getElementById('kullanici').value;
            var mesaj = document.getElementById('mesaj').value;
            socket.send(JSON.stringify({'kullanici': kullanici, 'mesaj': mesaj}));
            document.getElementById('mesaj').value = '';
        }
    </script>
</body>
</html>

# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'chat/index.html')

# chat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

# projenin ana urls.py dosyasında chat uygulamasını ekleyin
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
]


# Django Channels ile WebSockets destekli gerçek zamanlı uygulamalar geliştirilir.
# ASGI yapılandırması ile asenkron sunucu ayarlanır.
# Consumers ile WebSocket bağlantıları yönetilir.
# Group yapısı kullanılarak mesajlar tüm bağlı kullanıcılara iletilir.
# Frontend kısmında JavaScript ile WebSocket bağlantısı kurulur ve mesajlar gönderilir/alınır.