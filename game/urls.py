from django.urls import path

from game import views

urlpatterns = [
    path("", views.create_game, name="create_game"),
    path("<uuid:game_code>/", views.join_game, name="join_game"),
    path("<int:player_index>/<uuid:game_code>/", views.play_game, name="play_game"),
]
