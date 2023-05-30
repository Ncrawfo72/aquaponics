import digitalio
import time
import board
import adafruit_hcsr04
import neopixel
from PID_CPY import PID             

print(" hey ")  #this was an earlier test to test if are code was working
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2)    #our pins for are ultrasonic sensor
Kaz = neopixel.NeoPixel(board.NEOPIXEL, 1)     
KazOutput = 0
relaypin = digitalio.DigitalInOut(board.D8)
relaypin.direction = digitalio.Direction.OUTPUT

pid = PID( 0.5, -0.1, 0, setpoint = 24)    #where we enter our PID and then set our setpoint distance
PID.output_limits = (0, 1)

while True:
    try:
        Hi = pid(sonar.distance)      
        if Hi == 1 : 
            relaypin.value = True      #where the value effects if the valve is open or not
            print("open")
        else :
            relaypin.value = False    
            print("closed")
        time.sleep(0.1)         #the time our sesnor wait tells it senses again
    except RuntimeError:
        print("Retrying!")   #incase the distance found an error it would print retrying on the montior
    time.sleep(0.1)
