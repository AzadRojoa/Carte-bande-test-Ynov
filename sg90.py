from machine import Pin, PWM
import time


class SG90:
    def __init__(self, pin):
        self.sg90 = PWM(Pin(pin, mode=Pin.OUT))
        self.sg90.freq(50)
        self.start_time = time.ticks_us()

def TestSg90():
    sg = SG90(15)
    while time.ticks_us()-sg.start_time<10000000:
        sg.sg90.duty(26)
        time.sleep(1)
        sg.sg90.duty(123)
        time.sleep(1)


