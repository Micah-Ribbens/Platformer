from powerups.powerup import Powerup
from base.platformer_constants import AMMO_INCREASE_FROM_POWERUP


class AmmoPowerup(Powerup):
    """The powerup for giving the player more ammo"""

    def __init__(self, left_edge, top_edge):
        """Initializes the object"""

        super().__init__(left_edge, top_edge, "images/ammo_box.png")

    def run_player_collision(self, player):
        """Gives the player more ammo"""

        player.increase_ammo(AMMO_INCREASE_FROM_POWERUP)