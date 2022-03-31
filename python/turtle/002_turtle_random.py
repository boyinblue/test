import turtle
import time
import random

letters = [ "a", "b", "c", "d", "e", "f", "g" ]

def main():

    turtle.setup(width=640, height=480)

    cnt = 0
    while cnt < 10:
        rand_num = random.randrange(0, len(letters))
        turtle.write(letters[rand_num], True)
        time.sleep(1)
        cnt = cnt + 1

if __name__ == '__main__':
    main()
