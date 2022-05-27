#!/usr/bin/python
import time
import RPi.GPIO as GPIO
import pio
import Ports
#import serial
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pio.uart=Ports.UART () # Define serial port
'''
define pin for lcd
'''
# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005
delay = 0.5


# Define GPIO to LCD mapping
LCD_RS = 7
LCD_E  = 11
LCD_D4 = 12
LCD_D5 = 13
LCD_D6 = 15
LCD_D7 = 16
alcohol_Sensor = 18
relay = 22
seat_belt_Sensor = 29
vibration_sensor = 36
relay = 32
Buzzer= 31
switch=35
led=33

GPIO.setup(LCD_E, GPIO.OUT)  # E
GPIO.setup(LCD_RS, GPIO.OUT) # RS
GPIO.setup(LCD_D4, GPIO.OUT) # DB4
GPIO.setup(LCD_D5, GPIO.OUT) # DB5
GPIO.setup(LCD_D6, GPIO.OUT) # DB6
GPIO.setup(LCD_D7, GPIO.OUT) 

GPIO.setup(alcohol_Sensor, GPIO.IN) 
GPIO.setup(seat_belt_Sensor, GPIO.IN) 
GPIO.setup(vibration_sensor, GPIO.IN) 
GPIO.setup(relay , GPIO.OUT)
GPIO.setup(Buzzer, GPIO.OUT)
GPIO.setup(switch, GPIO.IN)
GPIO.setup(led ,  GPIO.OUT)
# Define some device constants
LCD_WIDTH = 20   # Maximum characters per line
LCD_CHR = True
LCD_CMD = False
LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 
LCD_LINE_3 = 0xD0

'''
Function Name :lcd_init()
Function Description : this function is used to initialized lcd by sending the different commands
'''
def lcd_init():
  # Initialise display
  lcd_byte(0x33,LCD_CMD) # 110011 Initialise
  lcd_byte(0x32,LCD_CMD) # 110010 Initialise
  lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
  lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
  lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,LCD_CMD) # 000001 Clear display
  time.sleep(E_DELAY)
'''
Function Name :lcd_byte(bits ,mode)
Fuction Name :the main purpose of this function to convert the byte data into bit and send to lcd port
'''
def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = data
  # mode = True  for character
  #        False for command
 
  GPIO.output(LCD_RS, mode) # RS
 
  # High bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x10==0x10:
    GPIO.output(LCD_D4, True)
  if bits&0x20==0x20:
    GPIO.output(LCD_D5, True)
  if bits&0x40==0x40:
    GPIO.output(LCD_D6, True)
  if bits&0x80==0x80:
    GPIO.output(LCD_D7, True)
 
  # Toggle 'Enable' pin
  lcd_toggle_enable()
 
  # Low bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x01==0x01:
    GPIO.output(LCD_D4, True)
  if bits&0x02==0x02:
    GPIO.output(LCD_D5, True)
  if bits&0x04==0x04:
    GPIO.output(LCD_D6, True)
  if bits&0x08==0x08:
    GPIO.output(LCD_D7, True)
 
  # Toggle 'Enable' pin
  lcd_toggle_enable()
'''
Function Name : lcd_toggle_enable()
Function Description:basically this is used to toggle Enable pin
'''
def lcd_toggle_enable():
  # Toggle enable
  time.sleep(E_DELAY)
  GPIO.output(LCD_E, True)
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)
  time.sleep(E_DELAY)
'''
Function Name :lcd_string(message,line)
Function  Description :print the data on lcd 
'''
def lcd_string(message,line):
  # Send string to display
 
  message = message.ljust(LCD_WIDTH," ")
 
  lcd_byte(line, LCD_CMD)
 
  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)

lcd_init()
lcd_string("Welcome Sir",LCD_LINE_1)
lcd_string("PSI  Project",LCD_LINE_2)
time.sleep(0.1)
lcd_byte(0x01,LCD_CMD) # 000001 Clear display
lcd_string("Smart Car System",LCD_LINE_1)
lcd_string("Activated",LCD_LINE_2)
time.sleep(0.1)
lcd_byte(0x01,LCD_CMD) # 000001 Clear display
if (GPIO.input(switch)==True):
      lcd_string("Switchoff falsealram",LCD_LINE_1)
      time.sleep(0.3)
      GPIO.output(led, True)
      GPIO.output(Buzzer,True)
lcd_byte(0x01,LCD_CMD) # 000001 Clear display
while 1:       

      # Print out results
      alcohol_data =  GPIO.input(alcohol_Sensor)
      seat_belt_data =  GPIO.input(seat_belt_Sensor)
      vibration_data =  GPIO.input(vibration_sensor)
      #switch=GPIO.input(switch)
      if(vibration_data == False):
        if(seat_belt_data == True):
          lcd_byte(0x01,LCD_CMD) # 000001 Clear display
          lcd_string("Seat Belt  Detected",LCD_LINE_1)
          lcd_string("Please DriveSafe ",LCD_LINE_2)
          lcd_string("    Happy journey",LCD_LINE_3)
          time.sleep(0.3)
          if(alcohol_data == True):
            lcd_string("Alcohol Detected  ",LCD_LINE_1)
            lcd_string("Accident Prevent ",LCD_LINE_2)
            lcd_string(" by Stopping Motor ",LCD_LINE_3)
            pio.uart.println("AT")
            pio.uart.println("AT+CMGF=1")
            pio.uart.println("AT+CMGS=\"123456789\"\r")
            pio.uart.println("Alcohol Detected ")    
            pio.uart.println("Stoped Motor")
            Data=pio.uart.recv()
            pio.uart.print(Data)
            GPIO.output(relay, False)
            GPIO.output(Buzzer, True)
            time.sleep(0.5)
            
          else:
            lcd_byte(0x01,LCD_CMD) # 000001 Clear display
            lcd_string("Vehicle Start ed",LCD_LINE_1)
            time.sleep(0.3)
            GPIO.output(Buzzer, False)
            GPIO.output(relay, True)
        else:
          lcd_byte(0x01,LCD_CMD) # 000001 Clear display
          lcd_string("Seat Belt not Detected",LCD_LINE_1)
          lcd_string("Safty First  ware seatbelt ",LCD_LINE_3)
          lcd_string("Stopping Motor ",LCD_LINE_2)
          GPIO.output(relay, False)			
          GPIO.output(Buzzer, True)
          time.sleep(0.5)
        
      elif(vibration_data == True):
        if(GPIO.input(switch)==False):
            GPIO.output(Buzzer, True)
            time.sleep(0.5)
            lcd_string("Accident detected ",LCD_LINE_1)
            lcd_string("Sending location  ",LCD_LINE_2)
            lcd_string("To   123456789 ",LCD_LINE_3)	
            pio.uart.println("AT")
            pio.uart.println("AT+CMGF=1")
            pio.uart.println("AT+CMGS=\"123456789\"\r")
            pio.uart.println("Accident Happened ")    
            pio.uart.println("location")  
        elif (GPIO.input(switch)==True):
          GPIO.output(Buzzer, False)
          lcd_string("Safe ",LCD_LINE_1)
          lcd_string("Sending SafeMessage ",LCD_LINE_2)
          lcd_string("To   123456789 ",LCD_LINE_3)	
          pio.uart.println("AT")
          pio.uart.println("AT+CMGF=1")
          pio.uart.println("AT+CMGS=\"123456789\"\r")
          pio.uart.println("Accident Not Happened ")   
          pio.uart.println("Safe, No need medical service ")			
        
        for x in range(1000):
          Data=pio.uart.recv()
          pio.uart.print(Data)

