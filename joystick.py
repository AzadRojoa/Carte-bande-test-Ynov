from machine import ADC,Pin
from lcd import LCD
import time

class JOYSTICK:
    def __init__(self, pins):
        self.xAxis = ADC(Pin(pins[0], Pin.IN)) # create an ADC object acting on a pin
        self.xAxis.atten(self.xAxis.ATTN_11DB)
        self.yAxis = ADC(Pin(pins[1], Pin.IN)) # create an ADC object acting on a pin
        self.yAxis.atten(self.yAxis.ATTN_11DB)
        self.button = Pin(pins[2], Pin.IN, Pin.PULL_UP)
        self.test = ["LED", "Microphone", "Buzzer", "Sg90", "7 Segments"]



    def validation(self,tab,i):
        displayLCD(self.test[i[0]])
        while self.button.value():
            prev_i = i[0]
            print(i[0])
            X = self.xAxis.read()
            Y = self.yAxis.read()
            if X> 2095 and Y != 0 and Y != 4095:
                i[0] = i[0]+1
            elif X< 1095 and Y != 0 and Y != 4095:
                i[0] = i[0]-1
            if i[0] < 0:
                i[0] = len(tab) + i[0]
            if i[0] > len(tab)-1:
                i[0] = i[0] - len(tab)
            time.sleep(0.1)
            if prev_i != i[0] :
                displayLCD(self.test[i[0]])
        displayTestLCD(self.test[i[0]])
        return tab[i[0]]()
    

def displayLCD(str):
    lcd = LCD(16,17,[5, 18, 19, 21, 22, 23, 32, 33])
    lcd.clear()
    lcd.write("Test : " + str)
    
def displayTestLCD(str):
    lcd = LCD(16,17,[5, 18, 19, 21, 22, 23, 32, 33])
    lcd.clear()
    lcd.write("Testing " + str)

