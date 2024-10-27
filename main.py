import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33, # type: ignore
    board.IO34, # type: ignore
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39    
   
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

for led in leds[:len(leds)//2+2]:
    led.value = True

arr = []
increment = 2727
#make array assigning specific values to each LED (20000-50000)
for i in range(11):
    value = 20000 + i * increment 
    arr.append(value)

# main loop
while True:
    volume = microphone.value
    print(volume)

    for i in range(11):
        if(volume > arr[i]):
            led[i].value = True
        else:
            led[i].value = False

        
    sleep(0.1)
        
    #make LEDS turn on based on volume input (if vol falls into x range make x,y,z LEDS turn on)
    # if volume > 



    # for i in range (len(leds)):
        
    #     leds[i].value = not leds[i].value
    #     print(i)
    #     print(leds[i].value)
    #     sleep(1)
    # instead of blinking,
    # how can you make the LEDs
    # turn on like a volume meter?