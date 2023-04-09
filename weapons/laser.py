from game_qu.base.events import TimedEvent
from game_qu.gui_components.component import Component

from weapons.weapon import Weapon


class Laser(Component, Weapon):
    """The laser for the enemy"""

    timed_event = None

    def __init__(self, user, path_to_image, object_type):

        # super().__init__()
        super().__init__(path_to_image)
        Weapon.__init__(self, 0, 0, 0, user, 0)
        self.object_type = object_type

        self.timed_event = TimedEvent(.07, False)

    def cause_damage(self, damage):
        pass

    def run(self):
        """Runs the laser"""

        print("RUN")

        self.timed_event.run(False, False)

        if self.timed_event.has_finished():
            self.length = 0

    def shoot(self, left_edge, top_edge, length, height):
        """Shoots the laser"""

        self.number_set_dimensions(left_edge, top_edge, length, height)

        self.timed_event.start()
