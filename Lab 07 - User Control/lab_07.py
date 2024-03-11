import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3


class Sun:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

        self.rooster_sound = arcade.load_sound('Rooster.wav')
        self.rooster_sound_player = None


    def draw(self):

        """ Sun """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius, self.
                                  color)
        arcade.draw_triangle_filled(self.position_x,
                                    self.position_y + (self.radius + 20),
                                    self.position_x + (self.radius + 10),
                                    self.position_y - (self.radius - 12),
                                    self.position_x - (self.radius + 10),
                                    self.position_y - (self.radius - 12),
                                    self.color)
        arcade.draw_triangle_filled(self.position_x,
                                    self.position_y - (self.radius + 20),
                                    self.position_x + (self.radius + 10),
                                    self.position_y + (self.radius - 12),
                                    self.position_x - (self.radius + 10),
                                    self.position_y + (self.radius - 12),
                                    self.color)

    def update(self):
        # Move the sun
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the sun hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius
            if not self.rooster_sound_player or not self.rooster_sound_player.playing:
                self.rooster_sound_player = arcade.play_sound(self.rooster_sound)

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius
            if not self.rooster_sound_player or not self.rooster_sound_player.playing:
                self.rooster_sound_player = arcade.play_sound(self.rooster_sound)

        if self.position_y < self.radius:
            self.position_y = self.radius
            if not self.rooster_sound_player or not self.rooster_sound_player.playing:
                self.rooster_sound_player = arcade.play_sound(self.rooster_sound)

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius
            if not self.rooster_sound_player or not self.rooster_sound_player.playing:
                self.rooster_sound_player = arcade.play_sound(self.rooster_sound)


class Moon:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):

        """ Moon """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius, self.
                                  color)
        arcade.draw_circle_filled(self.position_x + 15,
                                  self.position_y - 20,
                                  10,
                                  arcade.color.SLATE_GRAY)
        arcade.draw_circle_filled(self.position_x - 15,
                                  self.position_y + 20,
                                  15,
                                  arcade.color.SLATE_GRAY)
        arcade.draw_circle_filled(self.position_x - 15,
                                  self.position_y - 20,
                                  5,
                                  arcade.color.SLATE_GRAY)

    def update(self):

        # Move the sun
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the sun hits the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius


        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Rooster.wav
        self.rooster_sound = arcade.load_sound('rooster.wav')
        self.rooster_sound_player = None
        # Make the mouse disappear when it is over the window.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BABY_BLUE)

        # Create our sun
        self.sun = Sun(50, 50, 0, 0, 60, arcade.color.YELLOW)
        self.moon = Moon(50, 50, 0, 0, 60, arcade.color.LIGHT_GRAY)





    def on_draw(self):
        # Start render
        arcade.start_render()
        self.sun.draw()
        self.moon.draw()
        # Hill
        arcade.draw_circle_filled(400, -1500, 1800, arcade.color.LIGHT_GREEN)

    def update(self, delta_time):
        self.sun.update()
        self.moon.update()

    def on_key_press(self, key, modifiers):

        # Sun is controlled with Arrow keys
        if key == arcade.key.LEFT:
            self.sun.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.sun.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.sun.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.sun.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        # Sun release
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.sun.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.sun.change_y = 0

    def on_mouse_motion(self, x, y, dx, dy):
        self.moon.position_x = x
        self.moon.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            if not self.wolf_sound_player or not self.wolf_sound_player.playing:
                self.wolf_sound_player = arcade.play_sound(self.wolf_sound)


def main():
    window = MyGame(800, 600, "Lab 07")
    arcade.run()


main()
