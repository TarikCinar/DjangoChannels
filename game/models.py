import uuid

from django.db import models


class Game(models.Model):
    PLAYER_ONE = 1
    PLAYER_TWO = 2

    code = models.UUIDField(default=uuid.uuid4())
    player_one = models.CharField(max_length=50)
    player_two = models.CharField(max_length=50, null=True, blank=True)

    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.code}:{self.player_one} vs {self.player_two}"
