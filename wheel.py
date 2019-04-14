from time import sleep
import RPi.GPIO as gpio
from defines import ROTATION

from encoder import Encoder

class Wheel:

    def __init__(self , input1 , input2 , encoder_pin , forward_flags , reverse_flags):

        self.input1 = input1
        self.input2 = input2
        self.forward_flags = forward_flags
        self.reverse_flags = reverse_flags

        self._init_pins()

        self.encoder = Encoder(encoder_pin)

    def _init_pins(self):
        gpio.setup(self.input1 , gpio.OUT)
        gpio.setup(self.input2 , gpio.OUT)

    def forward(self):
        while self.encoder.is_state_updated() == False:
            gpio.output(self.input1 , self.forward_flags[0])
            gpio.output(self.input2 , self.forward_flags[1])

        self.stop()


    def reverse(self):

        while self.encoder.is_state_updated() == False:
            gpio.output(self.input1 , self.reverse_flags[0])
            gpio.output(self.input2 ,  self.reverse_flags[1])

        self.stop()


    def stop(self):
        gpio.output(self.input1 , False)
        gpio.output(self.input2 , False)


    def rotate_forward(self):
        state_count = self.encoder.get_state_count()
        final_count = state_count + ROTATION

        while state_count != final_count:
            self.forward()
            state_count += 1


    def rotate_reverse(self):
        state_count = self.encoder.get_state_count()
        final_count = state_count + ROTATION

        while state_count != final_count:
            self.reverse()
            state_count += 1


def main():


    gpio.setmode(gpio.BCM)
    wheel = Wheel(input1 = 22  , input2 = 27 , encoder_pin = MOTOR_ENCODER_1 , forward_flags =  [False , True] , reverse_flags =  [True , False])
    wheel2 = Wheel(input1 =  4 , input2 = 17 , encoder_pin = MOTOR_ENCODER_2 , forward_flags =  [True , False] , reverse_flags =  [False , True])

    '''
    wheel.rotate_forward()
    wheel2.rotate_forward()
    wheel.rotate_reverse()
    wheel2.rotate_reverse()
    '''

    wheel.forward()
    wheel2.forward()
    gpio.cleanup()


if __name__ == "__main__":
    main()
