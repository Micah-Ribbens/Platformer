from game_qu.base.library_changer import LibraryChanger

LibraryChanger.set_screen_dimensions(1100, 720)

# from ctypes import windll, c_int

from game_qu.base.game_runner_function import run_game
from platformer_screen import PlatformerScreen

# windll.shcore.SetProcessDpiAwareness(c_int(1))

run_game(PlatformerScreen())