import turtle
import random
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

functions = [draw_a, draw_e, draw_i, draw_o, draw_u]

def start():
    cnt = 0
    turtle.setup(600, 400)
    turtle.width(9)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-220, -30)
    while cnt < 10:
        ran_num = random.randrange(0, len(functions))
        functions[ran_num]()
        cnt = cnt + 1
        time.sleep(1)

if __name__ == '__main__':
    start()
