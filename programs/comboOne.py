#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Image, SoundFile, ImageFile
from time import sleep

def comboOne(library):
    #PSEUDOCODE
    #Reset motor angle
    #Drive until stalled
    #wait x amount of seconds
    #if motor angle is small:
    #   it is green
    #if motor angle is big:
    #   it is orage
    #if motor did not stall:
    #   it is blue
    #grab blue
    library.driveBase.drive(100, 0)
    while True:
        print("Left: " + str(library.leftDriveMotor.control.stalled()) + " Right: " + str(library.rightDriveMotor.control.stalled()))
        if library.leftDriveMotor.control.stalled() or library.rightDriveMotor.control.stalled():
            break
    library.driveBase.stop()

    pass