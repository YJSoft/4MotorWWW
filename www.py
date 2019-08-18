import traceback, struct
from time import time
from flask import Flask
from car import FourMotor
import RPi.GPIO as GPIO

wwwapp = Flask(__name__)
myCar = FourMotor()

@wwwapp.route("/")
def rootpage():
        return "OK"

@wwwapp.route("/move/<type>/<speed>")
def cmd_move(type, speed):
    speed = int(speed)
    if type == "forward":
        myCar.setSpeed(1,speed,1)
        myCar.setSpeed(2,speed,1)
        myCar.setSpeed(3,speed,0)
        myCar.setSpeed(4,speed,0)
    elif type == "backward":
        myCar.setSpeed(1,speed,0)
        myCar.setSpeed(2,speed,0)
        myCar.setSpeed(3,speed,1)
        myCar.setSpeed(4,speed,1)
    elif type == "left":
        myCar.setSpeed(1,speed,1)
        myCar.setSpeed(2,speed,0)
        myCar.setSpeed(3,speed,0)
        myCar.setSpeed(4,speed,1)
    elif type == "right":
        myCar.setSpeed(1,speed,0)
        myCar.setSpeed(2,speed,1)
        myCar.setSpeed(3,speed,1)
        myCar.setSpeed(4,speed,0)
    return "OK-Move"

if __name__ == '__main__':
    wwwapp.run(host='0.0.0.0', port=8088)
