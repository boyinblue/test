#!/usr/bin/env python3

from turtle import *
from abc import ABC, abstractmethod
import time

class Template(ABC):
    def draw_a(self):
        write("a", True)

    def draw_e(self):
        write("e", True)

    def draw_i(self):
        write("i", True)

    def draw_o(self):
        write("o", True)

    def draw_u(self):
        write("u", True)

    def draw(self):
        pass

    def start(self):
        setup(width=600, height=400)
        width(9)
        speed(0)
        penup()
        goto(-220, -30)
	
    def execute(self):
        self.start()
        self.draw()
        time.sleep(5)

if __name__ == '__main__':
    class TemplateImpl(Template):
        def draw(self):
            self.draw_a()
            self.draw_e()

    temp_impl = TemplateImpl()
    temp_impl.execute()
