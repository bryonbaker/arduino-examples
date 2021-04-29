from csinsc import *    # This library lets you use "goto" and "label"
import pyfirmata        # This library lets you talk to the Arduino
import time             # This library lets you pause the program

board = pyfirmata.Arduino('/dev/cu.usbmodem144201')

label .again

# Turn the LED on
board.digital[12].write(1)

# Sleep for 200 milli-seconds
time.sleep(0.2)

# Turn the LED off
board.digital[12].write(0)

# Sleep for 1 second
time.sleep(1)

# Loop forever
goto .again