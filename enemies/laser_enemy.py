from game_qu.base.utility_functions import load_and_transform_image, get_directional_path_to_image
from game_qu.gui_components.component import Component

from base.game_object import GameObject
from enemies.sights_enemy import SightsEnemy
# from weapons.bouncy_projectile_thrower import BouncyProjectileThrower
from base.platformer_constants import PLAYER_HEIGHT, STRAIGHT_ENEMY_HORIZONTAL_VELOCITY, LASER_ENEMY_LENGTH, LASER_ENEMY_HEIGHT
from weapons.laser import Laser


class LaserEnemy(SightsEnemy):
    """A ninja that throws projectiles that bounce"""
    
    laser = None

    def __init__(self, damage, hit_points, platform):
        """Initializes the object"""

        super().__init__(damage, hit_points, platform, base_image_path="images/laser_enemy")
        self.laser = Laser(self, "images/laser_right.png", "Enemy Weapon")
        load_and_transform_image("images/laser")

        self.length = LASER_ENEMY_LENGTH
        self.height = LASER_ENEMY_HEIGHT
        # self.weapon = BouncyProjectileThrower(lambda: False, self, STRAIGHT_ENEMY_HORIZONTAL_VELOCITY)

    @property
    def projectile_height(self):
        # Since all players should be the same height, then the first one can be safely chosen
        # because there has to be at least one player
        return PLAYER_HEIGHT / 2
    
    def do_action_at_end_of_path(self):
        """Does what the enemy is supposed to do at the end of the path"""
        
        super().do_action_at_end_of_path()
        laser_length = self.platform.length - self.length
        laser_left_edge = self.right_edge if self.is_facing_right else self.left_edge - laser_length
        laser_top_edge = self.vertical_midpoint
        self.laser.number_set_dimensions(laser_left_edge, laser_top_edge, laser_length, self.bottom_edge - laser_top_edge)
    
    def render(self):
        """Renders the object onto the screen"""

        super().render()
        self.laser.path_to_image = get_directional_path_to_image("images/laser", self.is_facing_right, "")
        self.laser.render()

    def update_for_side_scrolling(self, amount):
        """Updates all the objects for side scrolling"""

        self.laser.left_edge -= amount
        super().update_for_side_scrolling(amount)

    def run_action_at_start_of_path(self):
        """Runs the action at the start of the path"""

        self.laser.length = 0

    def get_collidable_components(self):
        """:returns: Component[]; all the components that the player can collide into"""

        return [self, self.laser]

    def run_enemy_collision(self, enemy, index_of_sub_component):
        """Runs what should happen when the player hits this object or the object's laser"""

        enemy.cause_damage(self.damage)

    def run_inanimate_object_collision(self, inanimate_object, index_of_sub_component):
        """Runs what should happen when the enemy collides with the top of the platform"""

        self.update_top_collision_data(inanimate_object)

        
        