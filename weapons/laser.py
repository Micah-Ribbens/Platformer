from game_qu.gui_components.component import Component

from weapons.weapon import Weapon


class Laser(Component, Weapon):
    """The laser for the enemy"""

    def __init__(self, user, path_to_image, object_type):

        # super().__init__()
        super().__init__(path_to_image)
        Weapon.__init__(self, 0, 0, 0, user, 0)
        self.object_type = object_type

    def cause_damage(self, damage):
        pass