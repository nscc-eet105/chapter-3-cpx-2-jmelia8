#Joe Melia EET-107

from adafruit_circuitplayground import cp
import time

pause = .3
black = (0, 0, 0)
red = (100, 0, 0)
blue = (0, 0, 100)
lights = 10

while True:
    for light in range(lights):
        cp.pixels[light] = blue
        time.sleep(pause)
        cp.pixels[light] = black
        time.sleep(pause)
    for light in range(lights -1, -1, -1):
        cp.pixels[light] = red
        time.sleep(pause)
        cp.pixels[light] = black
        time.sleep(pause)

        
