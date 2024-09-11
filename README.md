# IP_address
 MicroPython code to display the IP address of the raspberry pi on a 16x2 LCD 

Hardware components needed:
    •	Raspberry Pi 4
    •	I2C module for LCD (16 pins)
    •	LCD (16x2) (16 pins)
    •	10K and 1k resistors
    •	a 4 leg button
    •	jump wires
    

 PIN connection  (RASPI TO I2C LCD MODULE) 
    •	PIN4 to VCC
    •	PIN6 TO GND
    •	PIN3 TO SDA
    •	PIN5 TO SCL

Button connections
    •	lower right lef to 3.3V 
    •	upper right leg 10k resistor to ground 
    •	upper left leg 1k resito to GPIO 26

    
Install necessary librariy
•	sudo pip3 install RPLCD smbus2
Run this command to check I2C’s address
•	sudo i2cdetect -y 1

    