from game_qu.base.paths import ActionPath
from base.platformer_constants import *
from enemies.enemy import Enemy
from weapons.straight_projectile_thrower import StraightProjectileThrower


class SightsEnemy(Enemy):
    action_path = None
    length = STRAIGHT_ENEMY_LENGTH
    height = STRAIGHT_ENEMY_HEIGHT
    weapon = None
    is_facing_right = None
    is_gone = None

    # By default the Straight Enemy has this action_path, but the Bouncy Enemy has a different action_path
    def __init__(self, damage, hit_points, platform, velocity=STRAIGHT_ENEMY_HORIZONTAL_VELOCITY,
                 wait_time=STRAIGHT_ENEMY_ACTION_PATH_WAIT_TIME, base_image_path="images/sights_enemy"):

        """Initializes the object"""

        super().__init__(damage, hit_points, platform, base_image_path)
        self.number_set_dimensions(platform.left_edge, platform.top_edge - self.height, self.length, self.height)

        top_edge = platform.top_edge - self.height
        # Creating the action_path for the ninja
        self.action_path = ActionPath(Point(platform.right_edge - self.length, top_edge), self, velocity)
        self.action_path.add_point(Point(platform.left_edge, top_edge), self.run_action_at_start_of_path)
        self.action_path.add_point(Point(platform.left_edge, top_edge), self.do_action_at_end_of_path, wait_time)
        self.action_path.add_point(Point(platform.right_edge - self.length, top_edge), self.run_action_at_start_of_path)
        self.action_path.add_point(Point(platform.right_edge - self.length, top_edge), self.do_action_at_end_of_path, wait_time)

        self.action_path.is_unending = True
        # self.weapon = StraightProjectileThrower(lambda: False, self, STRAIGHT_ENEMY_HORIZONTAL_VELOCITY)
        # self.weapon.has_limited_ammo = False

    def update_for_side_scrolling(self, amount):
        """Updates the enemy after side scrolling,so nothing funky happens (like being on an invisible platform)"""

        self.action_path.update_for_side_scrolling(amount)
        # self.weapon.update_for_side_scrolling(amount)

    def hit_player(self, player, index_of_sub_component):
        pass

    def hit_by_player(self, player_weapon, index_of_sub_component):
        pass

    def run(self):
        """Runs everything necessary in order for this enemy to work"""

        self.action_path.run()
        # self.weapon.run()

    def get_components(self):
        """returns: Component[]; all the components of the straight enemy that should be rendered and ran"""

        return [self] + [self.health_bar]

    def do_action_at_end_of_path(self):
        """Does the action that is at the end of the path"""

        self.is_facing_right = not self.is_facing_right

    def run_action_at_start_of_path(self):
        """Runs the action at the start of the path"""

        pass

