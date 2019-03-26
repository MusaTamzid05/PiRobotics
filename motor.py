import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)

class Motor:

    def __init__(self , input1 , input2 , input3 , input4):

        self.input1 = input1
        self.input2 = input2
        self.input3 = input3
        self.input4 = input4

        self._init_pins()


    def _init_pins(self):


        gpio.setup(self.input1 , gpio.OUT)
        gpio.setup(self.input2 , gpio.OUT)
        gpio.setup(self.input3 , gpio.OUT)
        gpio.setup(self.input4 , gpio.OUT)

    def _cleanup_pin(self):
        gpio.cleanup()


    def forward(self):


        print("Moving forward.")
        gpio.output(self.input1 , True)
        gpio.output(self.input2 , False)
        gpio.output(self.input3 , True)
        gpio.output(self.input4 , False)


    def reverse(self):

        print("Moving backword.")
        gpio.output(self.input1 , False)
        gpio.output(self.input2 , True)
        gpio.output(self.input3 , False)
        gpio.output(self.input4 ,  True)

    def stop(self):

        gpio.output(self.input1 , False)
        gpio.output(self.input2 , False)
        gpio.output(self.input3 , False)
        gpio.output(self.input4 , False)




def main():


    motor1 = Motor(input1 = 22 , input2 = 27 , input3 = 17 , input4 = 4)
    motor1.forward()
    time.sleep(1.0)
    motor1.stop()


    motor1.reverse()
    time.sleep(1.0)
    motor1.stop()
    gpio.cleanup()

if __name__ == "__main__":
    main()
