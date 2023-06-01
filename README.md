# Robot Arm


* [Intro](#intro)
* [Planning](#planning)
* [Visuals](#visuals)
* [Code](#code)
* [Wiring](#wiring)
* [Reflection](#reflection)

---


## intro
This project was based around the idea of PID and our task was to build a system using PID to keep one variable in the system constant. We decided to do a aquaponics system with the controlled variable being the water level of the plant tank. Our system would be relatively simple, the entire system would be essentially enclosed inside a large 20 gallon fish tank. The tank would be partially filled with water that would act as a reservoir their would then be a smaller water tank inside that would have its water level controlled via a pump and valve using PID.



## Planning 
our planning was rather simple as the construction of our project was largely already made. The below pictures are our initial very rough sketch of the basis of our project, it will make much more sense once one views the completed project. The sketchs are faithful to our final project with the exception of the monitored tank being suspended instead of laying on some wood on the bottom 

<img src="https://github.com/cprocino/Aquaponics/assets/71406784/14a5ad63-bd11-4430-85fb-e59f7401c26c" height="200">


<img src="https://github.com/cprocino/Aquaponics/assets/71406784/925c8a53-bd52-4210-a16a-6adc7ba785c8" height="200">

our planning was slightly skewed by our knowledge of our lack of knowledge in PID 
for the first week after we desided on our project we would create the skeleton of our project using the fish tank and a few other household and lab idems.
the rest of the time we would spend trying to figure out how we would PID the project and how the new valves and pumps could be controlled with arduinos. 
our intitial plan was 
week 1: build the basics of the tank with a pump and the corect tubing and a controlable valve or pump to regulate water level

week 2: tweek pump and valve to maintain water level better(start with hand controls for PID)

week 3: start implementing PID

week 4-5: PID tuning

week 6: finish documentation and add plants









## visuals
<img src="https://github.com/cprocino/Aquaponics/assets/71406784/86a0e908-96a6-4de7-9fcf-735391fd2e29" height="300">

This is a partial picture of our wiring that shows the most important parts. ( see wiring diagram for full wiring) 

<img src="https://github.com/cprocino/Aquaponics/assets/71406784/e2a363ca-2033-448c-b5bb-e4b3e986a802" height="300">

This is the board we cut out in order fo make this a viable system for Hydro/aquaponics, it allows us to suspend potatos in the water and lets them grow.

<img src="https://github.com/cprocino/Aquaponics/assets/71406784/a56aafc4-da36-4c78-8105-d22c0ad17798" height="300">

This is a picture of our small monitiered tank and the valve we used to affect flow.

<img src="https://github.com/cprocino/Aquaponics/assets/71406784/99353b00-bdc5-4b77-abb7-96275dfcf8e0" height="250">

this is the tank that encloses the whole system.

<img src="https://github.com/cprocino/Aquaponics/assets/71406784/e11dadc4-419e-4fe5-b15d-2721fd8b6252" height="250">

this is our final pump, the one we first used was to strong and the valve could not keep up with the flow.

<img src="https://github.com/cprocino/Aquaponics/assets/71406784/ceef106a-32a8-4821-ae7c-09107d3ca763" height="250">

this is the whole project assembled with out the water or plants.

<img src="https://github.com/Ncrawfo72/aquaponics/blob/main/images/aquaponics%20working.gif" height="350">

A blurry video of our project pumping out water (Unfornatley you cant hear the clicking of our distance sensor working. However it is working)

## wiring 


<img src="https://github.com/cprocino/Aquaponics/assets/71406784/ab2396e1-eb2b-4488-9088-078385f6d8b5" height="350">

<img src="https://github.com/cprocino/Aquaponics/assets/71406784/e2b536a0-490c-4253-8386-be21ea5720ce" height="350">

(Our wiring may seem simple but its actually pretty complicated as we have both 12v and 6v in the same project and the added element of water and electricity)

  

## code

```
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
```

## reflection  





