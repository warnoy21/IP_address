# IP_address
 MicroPython code to display the IP address of the raspberry pi on a 16x2 LCD 

Hardware components needed:
    •	Raspberry Pi 4
    •	I2C module for LCD (16 pins)
    •	LCD (16x2) (16 pins)

 PIN connection  (RASPI TO I2C LCD MODULE) 
    •	PIN4 to VCC
    •	PIN6 TO GND
    •	PIN3 TO SDA
    •	PIN5 TO SCL
    
Install necessary librariy
•	sudo pip3 install RPLCD smbus2
Run this command to check I2C’s address
•	sudo i2cdetect -y 1

#check if wiring is correct and to tweak LCD resolution for visibility  
Test Code:

from RPLCD.i2c import CharLCD

#change the address if u have a different one.
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)
lcd.clear()

lcd.write_string('Hello, World!')
