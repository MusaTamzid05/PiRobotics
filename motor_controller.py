from wheel import Wheel
from defines import LEFT_INPUT_1
from defines import LEFT_INPUT_2
from defines import LEFT_ENCODER

from defines import  RIGHT_INPUT_1
from defines import  RIGHT_INPUT_2
from defines import RIGHT_ENCODER
import RPi.GPIO as gpio

class MotorController:

    def __init__(self):
        self.wheel1 = Wheel(input1 = LEFT_INPUT_1, input2 = LEFT_INPUT_2, encoder_pin = LEFT_ENCODER , forward_flags =  [False , True] , reverse_flags =  [True , False])
        self.wheel2 = Wheel(input1 =  RIGHT_INPUT_1 , input2 = RIGHT_INPUT_2, encoder_pin = RIGHT_ENCODER , forward_flags =  [True , False] , reverse_flags =  [False , True])


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

    total_state = 40
    gpio.setmode(gpio.BCM)

    try:

        motor_controller = MotorController()
        motor_controller.forward(state_count = total_state)
        motor_controller.reverse(state_count = total_state)
    finally:
        gpio.cleanup()

if __name__ == "__main__":
    main()

