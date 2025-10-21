from microbit import *
import random

while True:
    # Puedes cambiar esto por cualquier sensor, por ejemplo: temperature(), accelerometer.get_x(), etc.
    dato = random.randint(0, 100)
    print(dato)
    sleep(1000)
