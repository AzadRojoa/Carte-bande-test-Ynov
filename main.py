from microphone import MICROPHONE
from led import LED
from buzzer import BUZZER
from sg90 import SG90
from seven_segments import SevenSegments
import time


while True :
    seven = SevenSegments([13,12,14,27,26,25,33,32])
    seven.TestSevenSegments()
    time.sleep(1)
    led = LED(15)
    led.TestLed()
    time.sleep(1)
    micro = MICROPHONE(4,15)
    micro.TestMicrophone()
    time.sleep(1)
    buzzer = BUZZER(2)
    buzzer.TestBuzzerMario()
    time.sleep(1)
    sg = SG90(15)
    sg.TestSg90()
    time.sleep(1)