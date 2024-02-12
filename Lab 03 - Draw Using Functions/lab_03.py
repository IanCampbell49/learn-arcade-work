import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


def refraction():
    # Draw initial light
    arcade.draw_line(0, 300, 310, 425, arcade.color.WHITE, line_width=7)

    # Draw outer refraction
    # Red Refraction
    arcade.draw_polygon_filled([[474, 469], [800, 435], [800, 417], [467, 460]], arcade.color.RED)

    # Orange Refraction
    arcade.draw_polygon_filled([[467, 460], [800, 417], [800, 400], [460, 451]], arcade.color.ORANGE)

    # Yellow Refraction
    arcade.draw_polygon_filled([[460, 451], [800, 400], [800, 383], [453, 448]], arcade.color.YELLOW)

    # Green Refraction
    arcade.draw_polygon_filled([[453, 448], [800, 383], [800, 366], [446, 439]], arcade.color.BRIGHT_GREEN)

    # Blue Refraction
    arcade.draw_polygon_filled([[446, 439], [800, 366], [800, 349], [439, 430]], arcade.color.CG_BLUE)

    # Purple Refraction
    arcade.draw_polygon_filled([[439, 430], [800, 349], [800, 332], [432, 421]], arcade.color.MEDIUM_PURPLE)

    # Draw inner refraction
    arcade.draw_triangle_filled(473, 468, 292, 422, 513, 398, (255, 255, 255))


def prism(x, y):
    # Draw Prism
    arcade.draw_triangle_outline(x, y + 200, x - 200, y - 150, x + 200, y - 150, arcade.color.WHITE, border_width=5)
    arcade.draw_triangle_outline(x, y + 191, x - 192, y - 146, x + 192, y - 146, (83, 75, 79, 250), border_width=3)
    # arcade.draw_point(x, y, arcade.color.RED, 5)


def draw_refraction_slider(x, y):
    arcade.draw_rectangle_filled(x, y, 800, 400, arcade.color.BLACK)
    # arcade.draw_point(x, y, arcade.color.RED, 5)


def draw_name_slider(x, y):
    arcade.draw_rectangle_filled(x, y, 1600, 200, arcade.color.BLACK)
    # arcade.draw_point(x, y, arcade.color.RED, 5)


def name():
    # Text
    # I
    arcade.draw_line(40, 100, 40, 35, arcade.color.WHITE, line_width=4)
    arcade.draw_line(20, 100, 60, 100, arcade.color.WHITE, line_width=4)
    arcade.draw_line(20, 35, 60, 35, arcade.color.WHITE, line_width=4)

    # A
    arcade.draw_line(80, 35, 100, 100, arcade.color.WHITE, line_width=4)
    arcade.draw_line(100, 100, 120, 35, arcade.color.WHITE, line_width=4)
    arcade.draw_line(90, 65, 110, 65, arcade.color.WHITE, line_width=4)

    # N
    arcade.draw_line(150, 35, 150, 100, arcade.color.WHITE, line_width=4)
    arcade.draw_line(150, 100, 180, 35, arcade.color.WHITE, line_width=4)
    arcade.draw_line(180, 35, 180, 100, arcade.color.WHITE, line_width=4)

    # C
    arcade.draw_ellipse_outline(240, 65, 40, 65, arcade.color.WHITE, border_width=4)
    arcade.draw_rectangle_filled(260, 65, 20, 30, arcade.color.BLACK)

    # .
    arcade.draw_circle_filled(265, 35, 3, arcade.color.WHITE)


def on_draw(delta_time):
    """ Draw everything """
    arcade.start_render()

    refraction()
    draw_refraction_slider(on_draw.refraction_slider_x, 400)
    prism(400, 400)
    name()
    draw_name_slider(on_draw.name_slider_x, 50)

    on_draw.refraction_slider_x += 2
    on_draw.name_slider_x += 2


on_draw.refraction_slider_x = 400
on_draw.name_slider_x = 0


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.BLACK)

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1/60)
    arcade.run()



# Call the main function to get the program started.
main()
