from wheel import Wheel
from defines import MOTOR_ENCODER_1
from defines import MOTOR_ENCODER_2
import RPi.GPIO as gpio

class MotorController:

    def __init__(self):
        self.wheel1 = Wheel(input1 = 22  , input2 = 27 , encoder_pin = MOTOR_ENCODER_1 , forward_flags =  [False , True] , reverse_flags =  [True , False])
        self.wheel2 = Wheel(input1 =  4 , input2 = 17 , encoder_pin = MOTOR_ENCODER_2 , forward_flags =  [True , False] , reverse_flags =  [False , True])


    def forward(self , state_count = 1):

        current_state_count = 0

        while current_state_count != state_count:
            self.wheel1.forward()
            self.wheel2.forward()
            current_state_count += 1


    def reverse(self , state_count = 1):

        current_state_count = 0

        while current_state_count != state_count:
            self.wheel1.reverse()
            self.wheel2.reverse()
            current_state_count += 1



def main():

    gpio.setmode(gpio.BCM)
    motor_controller = MotorController()
    motor_controller.forward(state_count = 20)
    motor_controller.reverse(state_count = 20)
    gpio.cleanup()

if __name__ == "__main__":
    main()

