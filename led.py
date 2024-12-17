from machine import Pin,PWM
import time



class LED:
    def __init__(self, led):
        self.led = Pin(led, mode=Pin.OUT)
    
    def TestLed(self):
        for i in range(10):
            time.sleep(0.5)
            self.led.value(1)
            time.sleep(0.5)
            self.led.value(0)