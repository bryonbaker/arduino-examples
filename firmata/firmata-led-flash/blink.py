from csinsc import *
import pyfirmata
import time

board = pyfirmata.Arduino('/dev/cu.usbmodem144201')

# while True:
label .again

board.digital[12].write(1)
time.sleep(0.2)
board.digital[12].write(0)
time.sleep(1)

goto .again