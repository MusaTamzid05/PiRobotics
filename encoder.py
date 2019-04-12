import RPi.GPIO as GPIO
import time
import sys

STATE_PER_ROTATION = 40

class Encoder:

    def __init__(self , pin_number):
        self.pin_number = pin_number
        GPIO.setup(self.pin_number , GPIO.IN  , pull_up_down = GPIO.PUD_DOWN)
        self.state_count = 0
        self.last_state = GPIO.input(self.pin_number)

    def get_state_count(self):
        return self.state_count

    def is_state_updated(self):
        current_state = GPIO.input(self.pin_number)

        if current_state != self.last_state:
            self.last_state = current_state
            self.state_count += 1
            return True

        return False

    def update(self):
        self._update_state_count()
        print(self.state_count)
        #self._update_rotation()

    def _update_state_count(self):
        current_state = GPIO.input(self.pin_number)

        if current_state != self.last_state:
            self.last_state = current_state
            self.state_count += 1



    def _update_rotation(self):

        if self.state_count == STATE_PER_ROTATION:
            self.rotation_count += 1
            self.state_count = 0





def main():
    GPIO.setmode(GPIO.BCM)


    if len(sys.argv) != 2:
        print("Usage: pin_num")
        exit(1)

    pin_num = int(sys.argv[1])

    encoder = Encoder(pin_number = pin_num)

    try:
        while True:
            encoder.update()
            time.sleep(0.002)

    except KeyboardInterrupt:
        GPIO.cleanup()


if __name__ == "__main__":
    main()
