import RPi.GPIO as gpio
import time
from motor import Motor



def main():

    gpio.setmode(gpio.BCM)
    motor1 = Motor(input1 = 22 , input2 = 27 , input3 = 17 , input4 = 4)


    for i in range(3):

        print("Count :{}".format(i))
        motor1.forward()
        time.sleep(1.0)
        motor1.stop()


        motor1.reverse()
        time.sleep(1.0)
        motor1.stop()


        time.sleep(0.5)
    gpio.cleanup()

if __name__ == "__main__":
    main()
