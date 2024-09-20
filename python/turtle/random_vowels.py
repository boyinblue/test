#!/usr/bin/env python3

import random
#from vowel import Template
import vowel
import time

if __name__ == '__main__':
    class TemplateImpl(vowel.Template):
        def draw(self):
            functions = [self.draw_a, self.draw_e, self.draw_i, self.draw_o, self.draw_u]
            random.shuffle(functions)
            for i in range(0, len(functions)):
                functions[i]()
            time.sleep(5)

    temp_impl = TemplateImpl()
    temp_impl.execute()
