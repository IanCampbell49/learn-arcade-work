import random
import arcade

SPRITE_SCALING_PLAYER = 0.08
SPRITE_SCALING_COIN = 0.02
SPRITE_SCALING_SPIKE = 0.03
COIN_COUNT = 50
SPIKE_COUNT = 25

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        self.coin_sound = arcade.load_sound('coin.wav')
        self.coin_sound_player = None

        self.boom_sound = arcade.load_sound('boom.wav')
        self.boom_sound_player = None

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, 'Spite lab')

        self.player_list = None
        self.coin_list = None
        self.spike_list = None

        self.player_sprite = None
        self.spike_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BABY_BLUE)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.spike_list = arcade.SpriteList()

        self.score = 0
        # Set up the player
        self.player_sprite = arcade.Sprite('stone.jpg', SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range(SPIKE_COUNT):

            self.spike_sprite = arcade.Sprite('spiky-ball.jpg', SPRITE_SCALING_SPIKE)
            self.spike_sprite.center_x = random.randrange(SCREEN_WIDTH)
            self.spike_sprite.center_y = random.randrange(SCREEN_HEIGHT)

            self.spike_list.append(self.spike_sprite)

        for i in range(COIN_COUNT):
            coin = arcade.Sprite('coin.png', SPRITE_SCALING_COIN)
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            self.coin_list.append(coin)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()
        self.spike_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        if len(self.coin_list) == 0:
            arcade.draw_text('GAME OVER', 220, 300, arcade.color.WHITE, 50)

    def on_mouse_motion(self, x, y, dx, dy):

        if len(self.coin_list) != 0:

            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def update(self, delta_time):

        if len(self.coin_list) != 0:

            for coin in self.coin_list:
                coin.center_y += 2
                if coin.center_y > SCREEN_HEIGHT:
                    coin.center_y = 0
                    coin.center_x = random.randint(20, SCREEN_WIDTH - 20)

            for spiky in self.spike_list:
                spiky.center_x += 2
                if spiky.center_x > SCREEN_WIDTH:
                    spiky.center_x = 0
                    spiky.center_y = random.randint(20, SCREEN_HEIGHT - 20)

            self.coin_list.update()

            coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

            for coin in coins_hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1
                self.coin_sound_player = arcade.play_sound(self.coin_sound)

            self.spike_list.update()

            spidy_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.spike_list)

            for spidy in spidy_hit_list:
                spidy.remove_from_sprite_lists()
                self.score -= 1
                self.boom_sound_player = arcade.play_sound(self.boom_sound)






def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, 'Arcade lab 8')
    window.setup()
    arcade.run()


if __name__ == '__main__':
    main()
