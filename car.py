#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

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
GPIO.cleanup()

def setOutMode(port):
    global PWMS

    GPIO.setup(PORTS[port - 1][0], GPIO.OUT)
    GPIO.setup(PORTS[port - 1][1], GPIO.OUT)
    GPIO.output(PORTS[port - 1][0], GPIO.LOW)
    GPIO.output(PORTS[port - 1][1], GPIO.LOW)
    PWMS[port - 1] = GPIO.PWM(PORTS[port - 1][1], 1000)

def setSpeed(port, speed, direction):
    global PWMS
    global PWM_Status

    if direction == 1:
        GPIO.output(PORTS[port - 1][0], GPIO.HIGH)
    else:
        GPIO.output(PORTS[port - 1][0], GPIO.LOW)

    if speed > 0:
        if not PWM_Status[port - 1]:
            PWMS[port - 1].start(0)
            PWM_Status[port - 1] = True
        PWMS[port - 1].ChangeDutyCycle(speed)
    else:
        if PWM_Status[port - 1]:
            PWM_Status[port - 1] = False
            PWMS[port - 1].stop()

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    
    for i in range(1, 5):
        setOutMode(i)

    setSpeed(1,100,1)
    setSpeed(2,100,1)
    setSpeed(3,100,0)
    setSpeed(4,100,0)
    
    time.sleep(2)
    
    setSpeed(1,100,0)
    setSpeed(2,100,0)
    setSpeed(3,100,1)
    setSpeed(4,100,1)
    
    time.sleep(2)
    
    GPIO.cleanup()
