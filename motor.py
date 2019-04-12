import RPi.GPIO as gpio
import time
from encoder import Encoder
from defines import MOTOR_ENCODER_1


class Motor:

    def __init__(self , input1 , input2 , input3 , input4):

        self.input1 = input1
        self.input2 = input2
        self.input3 = input3
        self.input4 = input4

        self.moving = False
        self._init_pins()

        self.encoder2 = Encoder(pin_number = MOTOR_ENCODER_1 )

    def is_moving(self):
        return self.moving

    def set_moving(self , moving):
        self.moving = moving


    def _init_pins(self):


        gpio.setup(self.input1 , gpio.OUT)
        gpio.setup(self.input2 , gpio.OUT)
        gpio.setup(self.input3 , gpio.OUT)
        gpio.setup(self.input4 , gpio.OUT)

    def _cleanup_pin(self):
        gpio.cleanup()

    def _motor_forward1(self):
        gpio.output(self.input1 , False)
        gpio.output(self.input2 , True)

    def _motor_forward2(self):
        gpio.output(self.input3 , False)
        gpio.output(self.input4 ,  True)
        self.encoder2.update()

    def _motor_reverse1(self):
        gpio.output(self.input1 , True)
        gpio.output(self.input2 , False)

    def _motor_reverse2(self):
        gpio.output(self.input3 , True)
        gpio.output(self.input4 , False)
        self.encoder2.update()


    def reverse(self):

        print("Moving reverse.")
        self._motor_reverse1()
        self._motor_reverse2()


        self.moving = True


    def forward(self):
        print("Moving forward.")
        self._motor_forward1()
        self._motor_forward2()



        self.moving = True

    def stop(self):

        gpio.output(self.input1 , False)
        gpio.output(self.input2 , False)
        gpio.output(self.input3 , False)
        gpio.output(self.input4 , False)


        self.moving = False



def encoder_test():

    gpio.setmode(gpio.BCM)
    motor1 = Motor(input1 = 22 , input2 = 27 , input3 = 17 , input4 = 4)

    try:

        while True:
            motor1.forward()
            time.sleep(0.002)

    except KeyboardInterrupt:
        gpio.cleanup()



def main():

    gpio.setmode(gpio.BCM)

    motor1 = Motor(input1 = 22 , input2 = 27 , input3 = 17 , input4 = 4)
    motor1.forward()
    time.sleep(1.0)
    motor1.stop()


    motor1.reverse()
    time.sleep(1.0)
    motor1.stop()
    gpio.cleanup()

if __name__ == "__main__":
    encoder_test()
