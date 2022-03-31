import draw_shape
import turtle
import time

def draw_fire_engine():
  turtle.setup(width=1024, height=768)
  turtle.width(3)

  # 0 : Fastest, 1 : Slowest, 3 : slow, 6 : normal, 10 : fast
  turtle.speed(10)

  # 소방차 윤곽
  turtle.up()
  turtle.goto(-100, 0)
  turtle.down()
  turtle.right(90)
  turtle.forward(300)
  turtle.left(90)
  turtle.forward(550)
  turtle.left(90)
  turtle.forward(320)
  turtle.left(90)
  turtle.forward(500)
  turtle.left(45)
  turtle.goto(-100, 0)

  # 앞바퀴
  turtle.degrees()
  turtle.up()
  turtle.goto(50,-250)
  turtle.down()
  draw_shape.draw_wheel()

  # 앞바퀴 테두리
  turtle.up()
  turtle.goto(-20,-300)
  turtle.degrees()
  turtle.down()
  turtle.circle(50)

  # 뒷바퀴
  turtle.degrees()
  turtle.up()
  turtle.goto(350,-250)
  turtle.down()
  draw_shape.draw_wheel()

  # 뒷바퀴 테두리
  turtle.up()
  turtle.goto(320,-330)
  turtle.degrees()
  turtle.down()
  turtle.circle(50)

  # 호수
  turtle.degrees()
  turtle.up()
  turtle.goto(200,-150)
  turtle.down()
  draw_shape.draw_spiral_circles()

  time.sleep(3)

if __name__ == '__main__':
  draw_fire_engine()
