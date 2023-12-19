from gpiozero import LED
from time import sleep

LED = LED(15)

while True:
        LED.on()
        sleep(1.0)
        LED.off()
        sleep(1.0)
