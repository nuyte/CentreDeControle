import arcade
import argparse
from game.game import Game

parser = argparse.ArgumentParser(description='Some options for the program.')

parser.add_argument('--useKeyboard','-uk',action='store_true',default=False, \
                    help='If set, the keyboard can be used in addition to the '+\
                    'joystick ')
args = parser.parse_args()


FULLSCREEN = True
DEBUG_MODE = False
SCALE_SPEED = 0.0005
INIT_DELTA_TIME = 5

game = Game(fullscreen=FULLSCREEN, debug_mode=DEBUG_MODE, \
            scale_speed=SCALE_SPEED, init_delta_time=INIT_DELTA_TIME,\
            use_keyboard = args.useKeyboard)
game.setup()
arcade.run()
