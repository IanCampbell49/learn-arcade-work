# Import 'arcade' library
import arcade

# Open window 'lab_02'
arcade.open_window(800, 800, "lab_02")

# Background
arcade.set_background_color(arcade.color.BLACK)

# Start Drawing
arcade.start_render()

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

# Draw Prism
arcade.draw_triangle_outline(400, 600, 200, 250, 600, 250, arcade.color.WHITE, border_width=5)
arcade.draw_triangle_outline(400, 591, 208, 254, 592, 254, (83, 75, 79, 250), border_width=3)

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

# Finish Drawing
arcade.finish_render()


# Keep window open
arcade.run()
