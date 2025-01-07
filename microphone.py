from machine import Pin,PWM
import time



class MICROPHONE:
    def __init__(self, microphone, led):
        self.micro = Pin(microphone, mode=Pin.IN)
        self.start_time = time.ticks_us()
        self.led = Pin(led, mode=Pin.OUT)
    
def TestMicrophone():
    micro = MICROPHONE(4,15)
    while time.ticks_us()-micro.start_time<10000000:
        if micro.micro.value():
            micro.led.value(1)
        else:
            micro.led.value(0)
        time.sleep(0.1)
