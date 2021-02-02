import pyfirmata
import time

board = pyfirmata.Arduino('/dev/cu.usbmodem144101')

while True:
    board.digital[12].write(1)
    time.sleep(0.2)
    board.digital[12].write(0)
    time.sleep(1)