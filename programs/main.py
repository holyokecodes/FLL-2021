#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 UltrasonicSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Image, SoundFile, ImageFile

#import the library
from library import FUNCTION_LIBRARY

#import the combos
from comboOne import comboOne
from comboTwo import comboTwo
from comboThree import comboThree
from comboFour import comboFour

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# For more information:
# https://pybricks.github.io/ev3-micropython/

# Create your objects here.
ev3 = EV3Brick()
#motorA = Motor(Port.A)

#--MOTORS--
#Left Large Motor: C
#Right Large Motor: B
#Left Medium Motor: D
#Right Medium Motor: A
#--SENSORS--
#Left Color Sensor: 1
#Right Color Sensor: 2
#Bottom Gyroscope: 3
#Top Gyroscope: 4

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

ultrasonicSensor4 = UltrasonicSensor(Port.S4)

# Initialize the drive base.
robot = DriveBase(leftMotor, rightMotor, wheel_diameter=60, axle_track=200)

# init the library
library = FUNCTION_LIBRARY(robot, ev3, leftMotor, rightMotor, mediumMotorD, mediumMotorA, colorSensor1, colorSensor2, gyro3, ultrasonicSensor4)

library.calibrate()
ev3.screen.load_image(Image('GUI/ComboButtons.PNG'))

while True:
    buttons = ev3.buttons.pressed()
    if Button.LEFT in ev3.buttons.pressed():
        ev3.screen.load_image(Image('GUI/ComboOne.PNG'))
        comboOne(library)
        ev3.screen.load_image(Image('GUI/ComboButtons.PNG'))

    if Button.RIGHT in ev3.buttons.pressed():
        ev3.screen.load_image(Image('GUI/ComboTwo.PNG'))
        comboTwo(library)
        ev3.screen.load_image(Image('GUI/ComboButtons.PNG'))

    if Button.DOWN in ev3.buttons.pressed():
        ev3.screen.load_image(Image('GUI/ComboThree.PNG'))
        comboThree(library)
        ev3.screen.load_image(Image('GUI/ComboButtons.PNG'))

    if Button.UP in ev3.buttons.pressed():
        ev3.screen.load_image(Image('GUI/ComboFour.PNG'))
        comboFour(library)
        ev3.screen.load_image(Image('GUI/ComboButtons.PNG'))

