import arcade
from game.game import Game

FULLSCREEN = True
DEBUG_MODE = False
SCALE_SPEED = 0.0005
INIT_DELTA_TIME = 5

game = Game(fullscreen=FULLSCREEN, debug_mode=DEBUG_MODE, scale_speed=SCALE_SPEED, init_delta_time=INIT_DELTA_TIME)
game.setup()
arcade.run()
