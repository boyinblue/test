#!/usr/bin/env python3

import turtle
import time

turtle.setup(width=400, height=400)
turtle.width(3)
#turtle.speed(1)
#turtle.pendown()
turtle.speed(10)
turtle.pendown()
#turtle.goto(-220, -30)

def draw_square():
  for i in range(0,4):
    turtle.forward(100)
    turtle.left(90)

def draw_triangle():
  for i in range(0,3):
    turtle.forward(100)
    turtle.left(120)

def draw_star():
  for i in range(0,5):
    turtle.forward(100)
    turtle.left(144)

def draw_star_reverse():
  for i in range(0,5):
    turtle.forward(100)
    turtle.right(144)

def draw_pantagon():
  for i in range(0,5):
    turtle.forward(100)
    turtle.left(72)

def draw_sun():
  # 10
  for i in range(0,10):
    turtle.forward(100)
    turtle.left(108)

def draw_sun2():
  # 18
  for i in range(0,18):
    turtle.forward(100)
    turtle.left(140)

def draw_flower():
  # 36
  for i in range(0,36):
    turtle.forward(100)
    turtle.left(130)

def draw_star2():
  # 12
  for i in range(0,12):
    turtle.forward(100)
    turtle.left(150)

def draw_3d_star():
  for i in range(0,10):
    turtle.forward(100)
    turtle.left(145)

def draw_wheel():
  turtle.setup(width=400, height=400)
  for i in range(0,40):
    turtle.forward(100)
    turtle.left(145)

def draw_wheel2():
  for i in range(0,40):
    turtle.forward(100)
    turtle.left(144)

def draw_tier():
  turtle.speed(100)
  for i in range(0,90):
    turtle.forward(100)
    turtle.left(89)

def draw_circle():
  turtle.circle(100)

def draw_circles():
  for i in range(1,10):
    turtle.circle(10 * i)

def draw_spiral_circles():
  turtle.speed(0)
  for i in range(1,100):
    turtle.circle(i + 1, 45)

if __name__ == '__main__':
#  draw_square()
#  draw_pantagon()
#  draw_star()
#  draw_sun()
#  draw_sun2()
#  draw_flower()
#  draw_star2()
  draw_wheel()
#  draw_3d_star()
#  draw_star_reverse()
#  draw_tier()
#  draw_circle()
#  draw_circles()
#  draw_spiral_circles()
  time.sleep(3)
