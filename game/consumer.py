from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer

from game.models import Game


class GameConsumer(JsonWebsocketConsumer):
    PLAYER_ONE = 1
    PLAYER_TWO = 2

    def __create_unique_room_name(self):
        return str(self.game.code).replace('-', '')

    def connect(self):
        try:
            game_code = self.scope["url_route"]["kwargs"]["game_code"]
            player = self.scope["url_route"]["kwargs"]["player"]
            self.game = Game.objects.get(code=game_code)
            self.room_name = self.__create_unique_room_name()

            async_to_sync(self.channel_layer.group_add)(
                self.room_name, self.channel_name
            )

            self.accept()

            if player == self.PLAYER_TWO:
                async_to_sync(self.channel_layer.group_send)(
                    self.room_name, {"type": "send_player_two_join_game_info"}
                )

        except Game.DoesNotExist:
            self.disconnect(0)

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_name, self.channel_name
        )

    def receive_json(self, content, **kwargs):
        async_to_sync(self.channel_layer.group_send)(
            self.room_name, {"type": "send_json", "info": content}
        )

    def send_player_two_join_game_info(self, *args, **kwargs):
        self.send_json({
            "type": "player_two_join_game",
            "player_name": self.game.player_two
        })
