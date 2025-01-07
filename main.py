from lcd import LCD
from microphone import TestMicrophone
from led import TestLED
from buzzer import TestBuzzer
from sg90 import TestSg90
from seven_segments import TestSevenSegments
from joystick import JOYSTICK
import time

tab = [TestLED, TestMicrophone, TestBuzzer, TestSg90, TestSevenSegments]
i = [0]
while True :
    joy = JOYSTICK([12,14,26])
    joy.validation(tab,i)
    lcd = LCD(16,17,[5, 18, 19, 21, 22, 23, 32, 33])
    lcd.clear()
    lcd.write("Test finish")
    time.sleep(1)
    