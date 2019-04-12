import RPi.GPIO as GPIO
import time
import sys


class LED:

    def __init__(self , pin_num):
        self.pin_num = pin_num
        GPIO.setup(self.pin_num , GPIO.OUT)
        GPIO.output(self.pin_num , False)

    def turn_on(self):
        GPIO.output(self.pin_num , True)


    def turn_off(self):
        GPIO.output(self.pin_num , False)


def main():

    if len(sys.argv) !=  2:
        print("usage : pin_number")
        sys.exit(1)

    GPIO.setmode(GPIO.BCM)
    led = LED(pin_num = int(sys.argv[1]))


    try:

        while True:
            print("on")
            led.turn_on()
            time.sleep(1.0)
            print("off")
            led.turn_off()
            time.sleep(1.0)

    except KeyboardInterrupt:
        GPIO.cleanup()



if __name__ == "__main__":
    main()
