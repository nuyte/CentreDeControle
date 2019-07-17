import arcade
from .scaling_sprite import ScalingSprite
from game.jet import PosXJet, NegXJet, PosYJet, NegYJet

# ATV_IMG_WIDTH = 8822
# ATV_IMG_HEIGHT = 5881
# TARGET_IMG_POS_X = 4832
# TARGET_IMG_POS_Y = 2391


class ATV(ScalingSprite):

    def __init__(self, scale: float = 1, center_x: float = 0, center_y: float = 0):
        filename="./game/images/lightats.jpg"
        super().__init__(filename, scale, center_x, center_y)
        self.accelerations = [0, 0]
        self.jets = [PosXJet(), NegXJet(), PosYJet(), NegYJet()]

    def update(self):
        """
        Update the sprite.
        """
        self.change_x += self.acc_x
        self.change_y += self.acc_y
        self.center_x += self.change_x
        self.center_y += self.change_y
        self.angle += self.change_angle
        self.update_scale()
        self.update_jets()

    def draw(self):
        """ Draw the sprite. """
        arcade.draw_texture_rectangle(self.center_x, self.center_y,
                                      self.width, self.height,
                                      self.texture, self.angle, self.alpha,
                                      self.transparent,
                                      repeat_count_x=self.repeat_count_x,
                                      repeat_count_y=self.repeat_count_y)
        for jet in self.jets:
            jet.draw()

    def update_jets(self):
        for jet in self.jets:
            jet.update(self.scale, self.center_x, self.center_y, self.accelerations)
        self.accelerations = [0, 0]

    def _get_acc_x(self) -> float:
        """ Get the acceleration in the x axis of the sprite. """
        return self.accelerations[0]

    def _set_acc_x(self, new_value: float):
        """ Set the acceleration in the x axis of the sprite. """
        self.accelerations[0] = new_value

    acc_x = property(_get_acc_x, _set_acc_x)

    def _get_acc_y(self) -> float:
        """ Get the acceleration in the y axis of the sprite. """
        return self.accelerations[1]

    def _set_acc_y(self, new_value: float):
        """ Set the acceleration in the y axis of the sprite. """
        self.accelerations[1] = new_value

    acc_y = property(_get_acc_y, _set_acc_y)

    @property
    def target_pos_x(self):
        return self.center_x

    @property
    def target_pos_y(self):
        return self.center_y

    @property
    def target_radius(self):
        return 80 * self.scale
