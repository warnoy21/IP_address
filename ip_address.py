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
import Rpi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN,GPIO.IN)

# Initialize the LCD with the correct I2C expander and address
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, do>

def get_ip_address():
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Connect to an external server (doesn't send data)
        s.connect(("8.8.8.8", 80))
        # Get the IP address of the device
        ip_address = s.getsockname()[0]
    except Exception as e:
        # If there is an error, print it and return None
        print(f"Error: {e}")
        ip_address = None
    finally:
        # Close the socket
        s.close()

    return ip_address

if __name__ == "__main__":
    ip = get_ip_address()
    lcd.clear()
    if ip:
        # Clear the LCD and write the IP address
        lcd.write_string(f"{ip}")
        lcd.cursor_pos = (1,3 )  # (row, column) #indentation
        lcd.write_string('flsun.local') #replace to match your server
    #This will tell us if the raspi has a conenction to the wifii
    else:
        lcd.write_string("Could not determine IP address.")
