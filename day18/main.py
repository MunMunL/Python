# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as t
import random

color_list = [(229, 233, 240), (241, 229, 235), (227, 236, 231), (193, 164, 112), (143, 168, 186), (71, 90, 120), (131, 93, 57), (214, 206, 135), (185, 143, 157), (31, 39, 62), (71, 18, 33), (138, 66, 88), (118, 33, 55), (141, 179, 151), (156, 150, 67), (168, 102, 114), (46, 58, 94), (52, 33, 17), (68, 125, 106), (217, 176, 191), (180, 188, 215), (108, 119, 158), (75, 75, 36), (182, 89, 82), (215, 182, 175), (166, 200, 210), (96, 148, 118), (171, 204, 185), (97, 143, 150)]
t.colormode(255)
print(color_list[0])
t.shape("circle")
#t.hideturtle()
t.penup()
t.speed("fastest")

def row_print(a):
    for i in range(a):
        i += 1
        for j in range(a):
            t.color(random.choice(color_list))
            t.setposition(50 * j, 50 * i)
            t.stamp()

row_print(10)



t.exitonclick()