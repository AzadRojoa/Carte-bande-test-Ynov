from machine import Pin,PWM
import time



class LED:
    def __init__(self, led):
        self.led = Pin(led, mode=Pin.OUT)
    
def TestLED():
    led = LED(15)
    for i in range(10):
        time.sleep(0.5)
        led.led.value(1)
        time.sleep(0.5)
        led.led.value(0)
