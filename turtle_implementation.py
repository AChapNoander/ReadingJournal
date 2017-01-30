import turtle
import math

t = turtle.Turtle()


def square(turt, length):
    for i in range(4):
        turt.forward(length)
        turt.left(90)


def polygon(turt, sides, len, ratio):
    sides = int(sides * ratio)
    for i in range(sides):
        turt.forward(len)
        turt.left(360.0 / sides)


def circle(turt):
    for i in range(360):
        turt.forward(1)
        turt.left(1)


def circle_2(turt, radius, ratio):
    sides = 100
    length = (math.pi * 2 * radius) / sides
    polygon(turt, sides, length, ratio)


def arc(turt, degree):
    for i in range(degree):
        turt.forward(1)
        turt.left(1)


def pie_func(turt, n, l):
    radius = l/(2 * math.sin(math.pi / n))
    c_x = l/2
    c_y = math.sqrt(radius**2 - c_x**2)
    for i in range(n):
        turt.forward(l)
        turt.left((360.0 / n))
        hold = turt._position
        turt.setposition(c_x, c_y)
        turt.setposition(hold)


for i in range(3, 15):
    pie_func(t, i, 100)

turtle.mainloop()
