from lcd import LCD
from microphone import MICROPHONE
from led import LED
from buzzer import BUZZER
from sg90 import SG90
from seven_segments import SevenSegments
import time


while True :
    lcd = LCD(16,17,[5, 18, 19, 21, 22, 23, 32, 33])
    lcd.clear()
    lcd.write("Test 7 segments")
    seven = SevenSegments([13,12,14,27,26,25,33,32])
    seven.TestSevenSegments()
    time.sleep(1)
    lcd.clear()
    lcd.write("Test LED")
    led = LED(15)
    led.TestLed()
    time.sleep(1)
    lcd.clear()
    lcd.write("Test Microphone")
    micro = MICROPHONE(4,15)
    micro.TestMicrophone()
    time.sleep(1)
    lcd.clear()
    lcd.write("Test Buzzer")
    buzzer = BUZZER(2)
    buzzer.TestBuzzerMario()
    time.sleep(1)
    lcd.clear()
    lcd.write("Test Sg90")
    sg = SG90(15)
    sg.TestSg90()
    time.sleep(1)