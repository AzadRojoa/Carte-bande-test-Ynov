from machine import Pin
from time import sleep_ms

class LCD:

    def __init__(self, rs_pin, enable_pin, data_pins):
        """Initialisation du contrôleur HD44780."""
        self.rs = Pin(rs_pin, Pin.OUT)
        self.enable = Pin(enable_pin, Pin.OUT)
        self.data_pins = [Pin(pin, Pin.OUT) for pin in data_pins]
        self.rs.value(0)
        self.enable.value(0)
        for pin in self.data_pins:
            pin.value(0)
        self.initialize()

    def send_byte(self, value, is_data):
        """Envoie un octet au LCD."""
        self.rs.value(1 if is_data else 0)
        for i in range(8):
            self.data_pins[i].value((value >> i) & 0x01)
        self.pulse_enable()

    def pulse_enable(self):
        """Envoie une impulsion sur la broche ENABLE."""
        self.enable.value(0)
        sleep_ms(1)
        self.enable.value(1)
        sleep_ms(1)
        self.enable.value(0)

    def initialize(self):
        """Initialise le LCD (mode 8 bits)."""
        sleep_ms(20)  
        self.send_byte(0x38, is_data=False) 
        sleep_ms(5)
        self.send_byte(0x0C, is_data=False)
        sleep_ms(5)
        self.send_byte(0x01, is_data=False)
        sleep_ms(5)
        self.send_byte(0x06, is_data=False)

    def write(self, text):
        """Écrit une chaîne de caractères sur le LCD."""
        for char in text:
            self.send_byte(self.char_to_lcd_code_extended(char), is_data=True)

    def clear(self):
        """Efface l'écran du LCD."""
        self.send_byte(0x01, is_data=False)
        sleep_ms(2)
        
    def char_to_lcd_code_extended(self,c):
        special = ["!","\"","#","$","%","&","\'","(",")","*","+",",","-",".","/","`"]
        if 'a' <= c <= 'o':
            return 81 + ord(c) - ord('a')
        elif 'p' <= c <= 'z':
            return 208 + ord(c) - ord('p')
        if 'A' <= c <= 'O':
            return 17 + ord(c) - ord('A')
        elif 'P' <= c <= 'Z':
            return 144 + ord(c) - ord('P')
        elif '0' <= c <= '9':
            return 192 + ord(c) - ord('0')
        else:
            for i,valeur in enumerate(special):
                if valeur == c :
                    return 65 +i
                else :
                    return 300


if __name__ == "__main__":
    RS_PIN = 16
    ENABLE_PIN = 17
    DATA_PINS = [5, 18, 19, 21, 22, 23, 32, 33]
    lcd = LCD(RS_PIN, ENABLE_PIN, DATA_PINS)
    a = "ENFIN"
    lcd.write(a)




