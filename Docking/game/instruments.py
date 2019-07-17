import arcade
from .docking_system import DockingSystem
import numpy as np
import timeit


class Instruments:
    """
    Class allow drawing the visor within the screen.

    draw method should be called before other sprite's draw methods in order to keep the visor above all.

    """

    def __init__(self, docking_system: DockingSystem) -> None:
        self.docking_system = docking_system
        self.window = docking_system.window
        self.atv = docking_system.atv
        self.color = (204, 85, 0)

    def setup(self):
        self.draw_visor()

    def update(self):
        pass

    def draw(self):
        time_in = timeit.default_timer()
        self.drawState()
        time_state = timeit.default_timer()
        if self.window.debug:
            self.drawDebug()
        time_debug = timeit.default_timer()
        self.draw_visor()
        time_visor = timeit.default_timer()
        if self.docking_system.window.debug:
            print("Instrument state dt: " + str(time_state - time_in))
            print("Instrument debug dt: " + str(time_debug - time_state))
            print("Instrument visor dt: " + str(time_visor - time_debug))

    def draw_visor(self):
        arcade.draw_line(self.window.width / 2, 0,
                         self.window.width / 2, self.window.height,
                         self.color, 3)
        arcade.draw_line(0, self.window.height / 2,
                         self.window.width, self.window.height/2,
                         self.color, 3)

    def drawDebug(self):
        arcade.draw_point(self.atv.target_pos_x, self.atv.target_pos_y, arcade.color.BLUE, 10)
        arcade.draw_circle_outline(self.atv.target_pos_x, self.atv.target_pos_y, self.atv.target_radius,
                                   arcade.color.BLUE, 5)
        scale, position, velocity, is_initialised, is_initialising, is_docking_complete, is_on_target = \
            self.docking_system.get_properties()
        arcade.draw_text("Fps: " + str(np.round(self.window.fps)), 50, 110, arcade.color.WHITE, 12)
        arcade.draw_text("On target: " + str(is_on_target), 50, 95, arcade.color.WHITE, 12)
        arcade.draw_text("Initialised: " + str(is_initialised), 50, 80, arcade.color.WHITE, 12)
        arcade.draw_text("Initialising: " + str(is_initialising), 50, 65, arcade.color.WHITE, 12)
        arcade.draw_text("Docked: " + str(is_docking_complete), 50, 50, arcade.color.WHITE, 12)
        arcade.draw_text("Scale: " + str(scale), 50, 35, arcade.color.WHITE, 12)
        arcade.draw_text("Position: " + str(position), 50, 20, arcade.color.WHITE, 12)

    def drawState(self):
        _, _, _, _, is_initialising, is_dock, _ = self.docking_system.get_properties()
        if is_initialising:
            arcade.draw_text("REINITIALISATION", self.window.width/2, self.window.height / 2,
                             arcade.color.RED, 50, align='center',
                             anchor_x='center', anchor_y='center', rotation=0)
        if is_dock:
            arcade.draw_text("AMARRAGE REUSSI", self.window.width/2, self.window.height / 2,
                             arcade.color.GREEN, 50, align='center',
                             anchor_x='center', anchor_y='center', rotation=0)
