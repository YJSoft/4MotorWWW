import traceback, struct
from time import time
from flask import Flask
from car import setSpeed
from car import setOutMode
import RPi.GPIO as GPIO

wwwapp = Flask(__name__)

@wwwapp.route("/")
def rootpage():
        return "OK"

@wwwapp.route("/move/<type>/<speed>")
def cmd_move(type, speed):
    speed = int(speed)
    if type == "forward":
        setSpeed(1,speed,1)
        setSpeed(2,speed,1)
        setSpeed(3,speed,0)
        setSpeed(4,speed,0)
    elif type == "backward":
        setSpeed(1,speed,0)
        setSpeed(2,speed,0)
        setSpeed(3,speed,1)
        setSpeed(4,speed,1)
    elif type == "left":
        setSpeed(1,speed,1)
        setSpeed(2,speed,0)
        setSpeed(3,speed,0)
        setSpeed(4,speed,1)
    elif type == "right":
        setSpeed(1,speed,0)
        setSpeed(2,speed,1)
        setSpeed(3,speed,1)
        setSpeed(4,speed,0)
    return "OK"

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    
    for i in range(1, 5):
        setOutMode(i)
    
    wwwapp.run(host='0.0.0.0', port=8088)
