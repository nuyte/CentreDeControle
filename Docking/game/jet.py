import arcade


class Jet:

    def __init__(self) -> None:
        self.ATV_RADIUS = 2500
        self.start_x = 0
        self.start_y = 0
        self.end_x = 0
        self.end_y = 0
        self.is_active = False

    def update(self, scale, center_x, center_y, accelerations):
        pass

    def draw(self):
        if self.is_active:
            arcade.draw_line(self.start_x, self.start_y, self.end_x, self.end_y,
                             (178, 190, 181, 50), border_width=10)

    def check_activation(self, accelerations):
        pass


class PosXJet(Jet):

    def __init__(self) -> None:
        super().__init__()

    def update(self, scale, center_x, center_y, accelerations):
        self.start_x = center_x - self.ATV_RADIUS * scale
        self.end_x = center_x - self.ATV_RADIUS * 2 * scale
        self.start_y = center_y
        self.end_y = center_y
        self.is_active = self.check_activation(accelerations)

    def check_activation(self, accelerations):
        return accelerations[0] > 0


class NegXJet(Jet):

    def __init__(self) -> None:
        super().__init__()

    def update(self, scale, center_x, center_y, accelerations):
        self.start_x = center_x + self.ATV_RADIUS * scale
        self.end_x = center_x + self.ATV_RADIUS * 2 * scale
        self.start_y = center_y
        self.end_y = center_y
        self.is_active = self.check_activation(accelerations)

    def check_activation(self, accelerations):
        return accelerations[0] < 0


class PosYJet(Jet):

    def __init__(self) -> None:
        super().__init__()

    def update(self, scale, center_x, center_y, accelerations):
        self.start_x = center_x
        self.end_x = center_x
        self.start_y = center_y - self.ATV_RADIUS * scale
        self.end_y = center_y - self.ATV_RADIUS * 2 * scale
        self.is_active = self.check_activation(accelerations)

    def check_activation(self, accelerations):
        return accelerations[1] > 0


class NegYJet(Jet):

    def __init__(self) -> None:
        super().__init__()

    def update(self, scale, center_x, center_y, accelerations):
        self.start_x = center_x
        self.end_x = center_x
        self.start_y = center_y + self.ATV_RADIUS * scale
        self.end_y = center_y + self.ATV_RADIUS * 2 * scale
        self.is_active = self.check_activation(accelerations)

    def check_activation(self, accelerations):
        return accelerations[1] < 0
