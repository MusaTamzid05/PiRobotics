import RPi.GPIO as GPIO




def main():


    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()



if __name__ == "__main__":
    main()
