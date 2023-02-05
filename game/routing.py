from django.urls import path
from game.consumer import GameConsumer

urlpatterns = [
    path("<uuid:game_code>/<int:player>/", GameConsumer.as_asgi()),
]
