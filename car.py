#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

class FourMotor:
    M1_D = 6   # Physical 31
    M1_A = 12  # Physical 32
    M2_D = 13  # Physical 33
    M2_A = 21  # Physical 40
    M3_D = 19  # Physical 35
    M3_A = 16  # Physical 36
    M4_D = 26  # Physical 37
    M4_A = 20  # Physical 38

    PORTS = [[M1_D, M1_A],
             [M2_D, M2_A],
             [M3_D, M3_A],
             [M4_D, M4_A]]

    PWMS = [None] * 4
    PWM_Status = [False] * 4
    
    def __init__():
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        
        for i in range(1, 5):
            self.setOutMode(i)

    def setOutMode(self, port):
        GPIO.setup(self.PORTS[port - 1][0], GPIO.OUT)
        GPIO.setup(self.PORTS[port - 1][1], GPIO.OUT)
        GPIO.output(self.PORTS[port - 1][0], GPIO.LOW)
        GPIO.output(self.PORTS[port - 1][1], GPIO.LOW)
        self.PWMS[port - 1] = GPIO.PWM(self.PORTS[port - 1][1], 1000)

    def setSpeed(self, port, speed, direction):
        if direction == 1:
            GPIO.output(self.PORTS[port - 1][0], GPIO.HIGH)
        else:
            GPIO.output(self.PORTS[port - 1][0], GPIO.LOW)

        if speed > 0:
            if not self.PWM_Status[port - 1]:
                self.PWMS[port - 1].start(0)
                self.PWM_Status[port - 1] = True
            self.PWMS[port - 1].ChangeDutyCycle(speed)
        else:
            if self.PWM_Status[port - 1]:
                self.PWM_Status[port - 1] = False
                self.PWMS[port - 1].stop()

if __name__ == '__main__':
    myCar = FourMotor()

    myCar.setSpeed(1,100,1)
    myCar.setSpeed(2,100,1)
    myCar.setSpeed(3,100,0)
    myCar.setSpeed(4,100,0)
    
    time.sleep(2)
    
    myCar.setSpeed(1,100,0)
    myCar.setSpeed(2,100,0)
    myCar.setSpeed(3,100,1)
    myCar.setSpeed(4,100,1)
    
    time.sleep(2)
    
    GPIO.cleanup()
