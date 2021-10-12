#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Image, SoundFile, ImageFile

#import the library
from library import FUNCTION_LIBRARY

#import the combos
# from comboOne import *
# from comboTwo import *
# from comboThree import *
# from comboFour import *

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# For more information:
# https://pybricks.github.io/ev3-micropython/

# Create your objects here.
ev3 = EV3Brick()
#motorA = Motor(Port.A)

leftMotor = Motor(Port.B)
rightMotor = Motor(Port.C)
mediumMotorA = Motor(Port.A)
mediumMotorD = Motor(Port.D)

colorSensor1 = ColorSensor(Port.S1)
colorSensor2 = ColorSensor(Port.S2)

try:
    gyro3 = GyroSensor(Port.S3)
except:
    gyro3 = -1
    print("Error: Could not find GYROSCOPE of PORT 3")
try:
    gyro4 = GyroSensor(Port.S4)
except:
    gyro4 = -1
    print("Error: Could not find GYROSCOPE of PORT 4")

# Initialize the drive base.
robot = DriveBase(leftMotor, rightMotor, wheel_diameter=57.15, axle_track=115)

# init the library
library = FUNCTION_LIBRARY(robot, ev3, leftMotor, rightMotor, mediumMotorA, mediumMotorD, colorSensor1, colorSensor2, gyro3, gyro4)

library.calibrate()
ev3.screen.load_image(Image('GUI/ComboButtons.PNG'))

while True:
    buttons = ev3.buttons.pressed()
    if Button.LEFT in ev3.buttons.pressed():
        comboOne(robot, ev3, library, leftMotor, medium_motor, buttons)#, sensor_b, sensor_stop)
    if Button.RIGHT in ev3.buttons.pressed():
        comboTwo(robot, ev3, library, medium_motor, sensor_b, sensor_stop)
    if Button.UP in ev3.buttons.pressed():
        comboFour(robot, ev3, library, medium_motor)
    if Button.DOWN in ev3.buttons.pressed():
        comboThree(robot, ev3, library, medium_motor, sensor_b)

