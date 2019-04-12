from time import sleep
import RPi.GPIO as gpio
from defines import MOTOR_ENCODER_1
from encoder import Encoder


class Wheel:

    def __init__(self , input1 , input2 , encoder_pin):

        self.input1 = input1
        self.input2 = input2
        self._init_pins()

        self.encoder = Encoder(encoder_pin)

    def _init_pins(self):
        gpio.setup(self.input1 , gpio.OUT)
        gpio.setup(self.input2 , gpio.OUT)

    def forward(self):
        while self.encoder.is_state_updated() == False:
            gpio.output(self.input1 , False)
            gpio.output(self.input2 , True)

        self.stop()


    def reverse(self):
        gpio.output(self.input1 , True)
        gpio.output(self.input2 , False)


    def stop(self):
        gpio.output(self.input1 , False)
        gpio.output(self.input2 , False)



def main():


    gpio.setmode(gpio.BCM)
    wheel = Wheel(input1 = 22  , input2 = 27 , encoder_pin = MOTOR_ENCODER_1)
    wheel.forward()
    gpio.cleanup()


if __name__ == "__main__":
    main()
