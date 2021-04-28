# import colorgram
#
# #Colorgram allows extraction of specified number of colours from an image.
# colours = colorgram.extract('damienhirst.jpeg', 25)
#
# palette = []
# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     rgb_tuple = (r, g, b)
#     palette.append(rgb_tuple)
# print(palette)

from turtle import Turtle, Screen
import random

colour_list = [(225, 223, 225), (199, 175, 117), (212, 222, 215), (125, 36, 24), (223, 224, 228), (167, 106, 56), (186, 159, 52), (6, 57, 83), (108, 68, 85), (112, 161, 175), (21, 122, 174), (63, 153, 138), (39, 36, 35), (76, 40, 48), (9, 68, 47), (90, 141, 52), (182, 96, 79), (131, 38, 41), (141, 171, 156), (210, 200, 149), (179, 201, 186), (173, 153, 159), (212, 183, 176), (151, 114, 119)]

thomas = Turtle()
thomas.penup()
screen = Screen()
screen.colormode(255)
thomas.setheading(225)
thomas.forward(250)
thomas.setheading(0)

def row_up():
    thomas.left(90)
    thomas.forward(50)
    thomas.left(90)
    thomas.forward(500)
    thomas.right(180)


def move_horizontal():
    for i in range(10):
        rand_colour = random.choice(colour_list)
        thomas.dot(20, rand_colour)
        thomas.forward(50)


for row in range(10):
    move_horizontal()
    row_up()
thomas.hideturtle()
