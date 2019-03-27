import RPi.GPIO as GPIO

from time import time
from time import sleep

CM = 0.000058

class Sensor:

    def __init__(self , trigger_pin , echo_pin):
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin

        GPIO.setup(self.trigger_pin , GPIO.OUT)
        GPIO.setup(self.echo_pin , GPIO.IN)

    def _set_trigger(self):
        GPIO.output(self.trigger_pin , True)
        sleep(0.00001)
        GPIO.output(self.trigger_pin , False)

    def get_distance(self):

        try:
            self._set_trigger()
            return self._calculate_distance()
        except TypeError:
            return None


    def _calculate_distance(self):
        start_time = None
        stop_time = None

        while GPIO.input(self.echo_pin) == 0:
            start_time = time()

        while GPIO.input(self.echo_pin) == 1:
            stop_time = time()

        time_elasped = stop_time - start_time
        distance = round(time_elasped / CM  , 2 )

        return distance


def main():
    GPIO.setmode(GPIO.BCM)
    sensor = Sensor(trigger_pin = 20 , echo_pin = 16)


    try:

        while True:
            distance = sensor.get_distance()
            if distance is not None:
                print(distance)
                sleep(0.5)

    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
