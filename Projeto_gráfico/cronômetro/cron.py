import time
import os

class Cronometro:

    def __init__(self, s =0, min = 0, h = 0):
        self.s = s
        self.min = min
        self.h = h
    
    def __repr__(self):
        return f'{self.h:02d}:{self.min:02d}:{self.s:02d}'
    
    def incremento(self):
        self.s += 1

        if self.s >= 60:
            self.s = 0
            self.min +=1
        if self.min >= 60:
            self.min = 0
            self.h += 1
    
    def start(self):
        while True:
            os.system('cls')
            print(self)
            self.incremento()
            time.sleep(1)      
   


Cronometro1 = Cronometro()
Cronometro1.start()