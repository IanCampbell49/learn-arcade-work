import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprites and Random Bullets Example"
STARS_COUNT = 100
SPRITE_SCALING_STARS = 0.5
SPRITE_SCALING_LASER = 0.8
ENEMIES_COUNT = 25
BULLET_SPEED = 5


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)

        self.frame_count = 0
        self.player_list = None
        self.enemy_list = None
        self.bullet_list = None
        self.laser_list = None
        self.stars_list = None
        self.player = None

        self.score = 0
        self.lives = 3

        self.pexplosion_sound = arcade.load_sound('8 bit explosion.wav')
        self.pexplosion_sound_player = None

        self.bullet_sound = arcade.load_sound('player laser.wav')
        self.bullet_sound_player = None

        self.fail_sound = arcade.load_sound('fail music.wav')
        self.fail_sound_player = None

        self.aexplosion_sound = arcade.load_sound('alien explosion.wav')
        self.aexplosion_sound_player = None

        self.win_sound = arcade.load_sound('victory music.wav')
        self.win_sound_player = None

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.laser_list = arcade.SpriteList()
        self.stars_list = arcade.SpriteList()

        self.player = arcade.Sprite(":resources:images/space_shooter/playerShip1_orange.png", 0.5)
        self.player_list.append(self.player)

        for i in range(ENEMIES_COUNT):
            enemy = arcade.Sprite(":resources:images/space_shooter/playerShip1_green.png", 0.5)
            enemy.center_x = random.randrange(SCREEN_WIDTH)
            enemy.center_y = random.randrange(400, 600)
            enemy.angle = 180
            self.enemy_list.append(enemy)

        for i in range(STARS_COUNT):
            stars = arcade.Sprite(':resources:images/space_shooter/meteorGrey_tiny1.png', SPRITE_SCALING_STARS)
            stars.center_x = random.randrange(SCREEN_WIDTH)
            stars.center_y = random.randrange(SCREEN_HEIGHT)

            self.stars_list.append(stars)

    def on_draw(self):

        self.clear()

        self.stars_list.draw()
        self.enemy_list.draw()
        self.bullet_list.draw()
        self.laser_list.draw()
        self.player_list.draw()

        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)
        arcade.draw_text(f"Lives: {self.lives}", 100, 20, arcade.color.WHITE, 14)

        if len(self.enemy_list) == 0:

            arcade.draw_lrtb_rectangle_filled(0, 800, 600, 0, arcade.color.BLACK)
            arcade.draw_text("CONGRATULATIONS!", 50, 300, arcade.color.WHITE, 50)
            arcade.draw_text("YOU WIN!", 200, 200, arcade.color.WHITE, 50)
            arcade.draw_text(f"Final Score: {self.score}", 250, 150, arcade.color.WHITE, 25)

            if not self.win_sound_player or not self.win_sound_player.playing:
                self.win_sound_player = arcade.play_sound(self.win_sound)

        if self.lives <= 0:
            arcade.draw_lrtb_rectangle_filled(0, 800, 600, 0, arcade.color.BLACK)
            arcade.draw_text("TOO BAD!", 220, 300, arcade.color.WHITE, 50)
            arcade.draw_text("YOU LOST!", 200, 200, arcade.color.WHITE, 50)
            if not self.fail_sound_player or not self.fail_sound_player.playing:
                self.fail_sound_player = arcade.play_sound(self.fail_sound)

    def on_mouse_press(self, x, y, button, modifiers):

        bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png", SPRITE_SCALING_LASER)

        bullet.angle = 90

        bullet.change_y = BULLET_SPEED

        bullet.center_x = self.player.center_x
        bullet.bottom = self.player.top

        self.bullet_list.append(bullet)
        arcade.play_sound(self.bullet_sound)

    def on_update(self, delta_time):

        if len(self.stars_list) != 0:

            for stars in self.stars_list:
                stars.center_y += 2
                if stars.center_y > SCREEN_HEIGHT:
                    stars.center_y = 0
                    stars.center_x = random.randint(20, SCREEN_WIDTH - 20)

            for enemy in self.enemy_list:
                enemy.center_x += 2
                if enemy.center_x > SCREEN_WIDTH:
                    enemy.center_x = 0
                    enemy.center_y = random.randrange(400, 600)

        for enemy in self.enemy_list:

            odds = 200

            adj_odds = int(odds * (1 / 30) / delta_time)

            if random.randrange(adj_odds) == 0:
                if self.lives == 0:
                    arcade.draw_text('Game over', 300, 300, arcade.color.WHITE, 100)

                else:

                    laser = arcade.Sprite(":resources:images/space_shooter/laserRed01.png")

                    laser.center_x = enemy.center_x

                    laser.angle = 180

                    laser.top = enemy.bottom

                    laser.change_y = -2

                    self.laser_list.append(laser)

        if len(self.enemy_list) != 0:

            for bullet in self.bullet_list:
                if bullet.top < 0:
                    bullet.remove_from_sprite_lists()

            self.bullet_list.update()

            for bullet in self.bullet_list:

                bullet_hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)

                if len(bullet_hit_list) > 0:
                    bullet.remove_from_sprite_lists()

                for enemy in bullet_hit_list:
                    enemy.remove_from_sprite_lists()
                    self.score += 1
                    arcade.play_sound(self.aexplosion_sound)

                if bullet.bottom > SCREEN_HEIGHT:
                    bullet.remove_from_sprite_lists()

        for laser in self.laser_list:
            laser_hit_list = arcade.check_for_collision_with_list(laser, self.player_list)

            if len(laser_hit_list) > 0:
                laser.remove_from_sprite_lists()

            for player in laser_hit_list:
                self.lives -= 1
                arcade.play_sound(self.pexplosion_sound)

        self.laser_list.update()

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """ Called whenever the mouse moves. """
        if len(self.enemy_list) != 0:
            self.player.center_x = x
            self.player.center_y = y


def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

"""all outsourced code was retived from the arcade library"""
"""all sounds were taken from freesound.com"""
