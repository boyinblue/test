import turtle
import time

def draw_star():
  for i in range(0,5):
    turtle.forward(100)
    turtle.left(144)

  time.sleep(5)

if __name__ == '__main__':
  draw_star()
