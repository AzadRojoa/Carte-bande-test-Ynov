from machine import Pin,PWM
import time

class SevenSegments:

    def __init__(self, pins):
        self.tab = pins

            
    def InitialisePins(self):
        for i in self.tab:
            pin = Pin(i, mode=Pin.OUT)
            pin.value(0)


    def TestSevenSegments(self):
        self.InitialisePins()
        for i in self.tab:
            time.sleep(0.5)
            pin = Pin(i, mode=Pin.OUT)
            pin.value(1)
        time.sleep(2)
        self.InitialisePins()
