from machine import Pin,PWM
import time



class MICROPHONE:
    def __init__(self, microphone, led):
        self.micro = Pin(microphone, mode=Pin.IN)
        self.start_time = time.ticks_us()
        self.led = Pin(led, mode=Pin.OUT)
    
    def TestMicrophone(self):
        while time.ticks_us()-self.start_time<10000000:
            if self.micro.value():
                self.led.value(1)
            else:
                self.led.value(0)
            time.sleep(0.1)