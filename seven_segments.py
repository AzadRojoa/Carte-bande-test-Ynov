from machine import Pin,PWM
import time

class SevenSegments:

    def __init__(self, pins):
        self.tab = pins

            
    def InitialisePins(self):
        for i in self.tab:
            pin = Pin(i, mode=Pin.OUT)
            pin.value(0)


def TestSevenSegments():
    segments = SevenSegments([13,12,14,27,26,25,33,32])
    segments.InitialisePins()
    for i in segments.tab:
        time.sleep(0.5)
        pin = Pin(i, mode=Pin.OUT)
        pin.value(1)
    time.sleep(2)
    segments.InitialisePins()

