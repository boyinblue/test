import turtle
import time

def draw_a():
    turtle.write("a", True)

def draw_e():
    turtle.write("e", True)

def draw_i():
    turtle.write("i", True)

def draw_o():
    turtle.write("o", True)

def draw_u():
    turtle.write("u", True)

def start():
    cnt = 0
    turtle.setup(width=600, height=400)
    turtle.width(9)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-220, -30)
    while cnt < 10:
        draw_e()
        draw_o()
        draw_u()
        time.sleep(1)
        cnt = cnt + 1

if __name__ == '__main__':
    start()
