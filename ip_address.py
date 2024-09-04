#####################################################
# MicroPython that for Raspberry pi 4 that programs an I2C LCD module to display it's IP address and 
# local's server when connected to the wifii or let the user know it isnt connected to wifii for 3D printing to
# avoid the annoyance of plugging in a monitor or using ssh tools to find out the IP once the 3D printer was not put on
# used for a long time.
#
# Made by : Dabakama_Mindset         
# Date    : September 2,2024
#
#####################################################



from RPLCD.i2c import CharLCD
import socket
import RPi.GPIO as GPIO
import time
BUTTON_PIN = 26 #change based on the GPIO to be used
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN,GPIO.IN)

# Initialize the LCD with the correct I2C expander and address
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)

def get_ip_address():
    """
    Get it's Ip address
    return: the IP address ,else None
    """
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Connect to an external server (doesn't send data)
        s.connect(("8.8.8.8", 80))
        # Get the IP address of the device
        ip_address = s.getsockname()[0]
    except Exception as e:
        # If there is an error, return None
        ip_address = None
    finally:
        # Close the socket
        s.close()

    return ip_address

def display_ip():
    """
    Displays the IP address and server name , else no wifii
    return: NA
    """

    ip = get_ip_address()
    if ip:
        lcd.write_string(ip)
        lcd.cursor_pos = (1, 3)  # (row, column)
        lcd.write_string('flsun.local')
    else:
        lcd.write_string("Could not determine IP address.")
if __name__ == "__main__":

    display_ip()

    while True:
        #if reset button pressed, it retries to obtain its IP
        if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
           lcd.clear()
           print("pressed") # debugging
           time.sleep(0.2) #to give a flick for UI
           display_ip()
           
           # Wait for a short period to debounce the button
           time.sleep(0.5)

            # Optional: add a small delay to reduce CPU usage
    time.sleep(1)