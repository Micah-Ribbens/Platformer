from enemies.sights_enemy import StraightEnemy
# from weapons.bouncy_projectile_thrower import BouncyProjectileThrower
from base.platformer_constants import PLAYER_HEIGHT, STRAIGHT_ENEMY_HORIZONTAL_VELOCITY


class BouncyEnemy(StraightEnemy):
    """A ninja that throws projectiles that bounce"""

    def __init__(self, damage, hit_points, platform):
        """Initializes the object"""

        super().__init__(damage, hit_points, platform, base_image_path="images/laser_enemy")
        # self.weapon = BouncyProjectileThrower(lambda: False, self, STRAIGHT_ENEMY_HORIZONTAL_VELOCITY)

    @property
    def projectile_height(self):
        # Since all players should be the same height, then the first one can be safely chosen
        # because there has to be at least one player
        return PLAYER_HEIGHT / 2
