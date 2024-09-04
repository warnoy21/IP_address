#check if wiring is correct and to tweak LCD resolution for visibility  


from RPLCD.i2c import CharLCD

#change the address if u have a different one.
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)
lcd.clear()

lcd.write_string('Hello, World!')
