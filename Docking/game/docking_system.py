import arcade
from .atv import ATV

import numpy as np

XY_TOL = 20
DOCKING_SCALE = 1.5


class DockingSystem:

    def __init__(self, arcade_window: arcade.Window, atv: ATV,
                 init_scale: float = 1, init_pos_x: float = 0, init_pos_y: float = 0,
                 scale_speed: float = 0.001, init_delta_time: float = 10) -> None:
        self.window = arcade_window
        self.atv = atv
        self.init_scale = init_scale
        self.init_pos_x = init_pos_x
        self.init_pos_y = init_pos_y
        self.scale_speed = scale_speed
        self.init_delta_time = init_delta_time * 60
        self.is_initialised = True
        self.is_initialising = False
        self.is_docking_complete = False

    def update(self):
        self.update_approach()
        if self.is_initialising:
            self.update_initialisation()
        elif self.is_target_hit():
            self.dock()
        elif self.outside_window():
            self.is_initialising = True
            self.reinitialisation()

    def update_initialisation(self):
        if self.is_initialized():
            self.is_initialising = False
            self.is_initialised = True
            self.atv.with_perspective = True
            self.stop()

    def update_approach(self):
        if self.is_initialised and (self.atv.change_x != 0 or self.atv.change_y != 0):
            self.is_initialised = False
            self.atv.change_z = self.scale_speed

    def is_on_target(self):
        distance_to_target = self.distance_to_target(self.window.width / 2, self.window.height / 2)
        return distance_to_target < self.atv.target_radius

    def is_target_hit(self):
        return self.is_on_target() and (self.atv.scale > DOCKING_SCALE)

    def is_initialized(self):
        return abs(self.atv.center_x - self.init_pos_x) < XY_TOL \
               and abs(self.atv.center_y - self.init_pos_y) < XY_TOL \
               and (self.atv.scale < self.init_scale)

    def outside_window(self):
        return (self.atv.center_x < 0) or (self.atv.center_x > self.window.width) \
               or (self.atv.center_y < 0) or (self.atv.center_y > self.window.height) \
               or (self.atv.scale > DOCKING_SCALE)

    def dock(self):
        self.stop()
        self.is_docking_complete = True

    def distance_to_target(self, x, y):
        return np.sqrt((x - self.atv.target_pos_x)**2 + (y - self.atv.target_pos_y)**2)

    def stop(self):
        self.atv.change_x, self.atv.change_y, self.atv.change_z = 0, 0, 0

    def reinitialisation(self):
        self.atv.with_perspective = False
        self.atv.change_z = (self.init_scale - self.atv.scale) / self.init_delta_time
        self.atv.change_x = (self.init_pos_x - self.atv.center_x) / self.init_delta_time
        self.atv.change_y = (self.init_pos_y - self.atv.center_y) / self.init_delta_time

    def get_properties(self):
        return self.atv.scale, self.atv.position, self.atv.velocity, \
               self.is_initialised, self.is_initialising, self.is_docking_complete, self.is_on_target()
