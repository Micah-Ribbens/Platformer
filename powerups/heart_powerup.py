from powerups.powerup import Powerup
from base.platformer_constants import HEALTH_INCREASE_FROM_HEART


class HeartPowerup(Powerup):
    """The powerup for giving the player more health"""

    def __init__(self, left_edge, top_edge):
        """Initializes the object"""

        super().__init__(left_edge, top_edge, "images/heart.png")

    def run_player_collision(self, player):
        """Gives the player more health"""

        player.increase_health(HEALTH_INCREASE_FROM_HEART)