#!/usr/bin/env python3

import turtle
import time

def start():
    cnt = 0
    turtle.setup(width=600, height=400)
    turtle.width(9)
    turtle.speed(1)
    turtle.penup()
    while cnt < 100:
        turtle.forward(cnt)
        turtle.right(90)
        time.sleep(0.1)
        cnt = cnt + 1

if __name__ == '__main__':
    start()
