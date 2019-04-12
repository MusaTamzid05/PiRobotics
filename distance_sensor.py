from sensor import Sensor


from defines import TRIGGER_PIN
from defines import ECHO_PIN
from defines import MIN_DISTANCE
from defines import MAX_DISTANCE
from defines import DISTANCE_SLEEP
from defines import CLOSE_DISTANCE
from defines import FAR_DISTANCE

import RPi.GPIO as gpio
from time import sleep
from motor import Motor


class DistanceSensor:
    def __init__(self):
        self.min_distance = MIN_DISTANCE
        self.max_distance = MAX_DISTANCE
        self.close_distance = CLOSE_DISTANCE
        self.far_distance = FAR_DISTANCE
        self.sensor = Sensor(trigger_pin = TRIGGER_PIN , echo_pin = ECHO_PIN)

    def get_distance(self):
        return self.sensor.get_distance()

    def is_in_range(self , current_distance):
        return current_distance >= self.min_distance and current_distance <= self.max_distance

    def is_far(self , current_distance):
        return current_distance > self.far_distance


    def is_close(self , current_distance):
        return current_distance <  self.close_distance



def main():
    gpio.setmode(gpio.BCM)
    distance_sensor = DistanceSensor()
    motor = Motor(input1 = 22 , input2 = 27 , input3 = 17 , input4 = 4)

    try:
        while True:
                distance = distance_sensor.get_distance()

                if distance is None:
                    print("None")
                    sleep(DISTANCE_SLEEP)
                    continue

                if distance_sensor.is_in_range(distance) == False:
                    sleep(DISTANCE_SLEEP)
                    continue


                if distance_sensor.is_far(distance):
                    print("Forward")
                    motor.forward()
                    sleep(DISTANCE_SLEEP)
                    motor.stop()
                    continue


                if distance_sensor.is_close(distance):
                    print("Backword")
                    motor.reverse()
                    sleep(DISTANCE_SLEEP)
                    motor.stop()
                    continue


                print("....")

                sleep(DISTANCE_SLEEP)

    except KeyboardInterrupt:
            gpio.cleanup()


def test():
    gpio.setmode(gpio.BCM)
    distance_sensor = DistanceSensor()
    motor = Motor(input1 = 22 , input2 = 27 , input3 = 17 , input4 = 4)


    while True:
        motor.forward()
if __name__ == "__main__":
    main()
