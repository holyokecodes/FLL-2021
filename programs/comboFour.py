#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Image, SoundFile, ImageFile

def comboFour(library):
   #Go up to the line to line follow
    library.driveBase.straight(library.inchToMM(6.5))
    library.turn(40, 100) 
    library.driveBase.straight(library.inchToMM(8)) 

    library.lineFollowForDistance(distance=library.inchToMM(17.35),DRIVE_SPEED=120,p=-.9,sensor_lf=library.colorSensor1)
    library.rightAttachment.run_angle(-60, 30)
    library.lineFollowForDistance(distance=library.inchToMM(5.15),DRIVE_SPEED=120,p=-.9,sensor_lf=library.colorSensor1)
    library.rightAttachment.run_angle(-60, 30)
    library.lineFollowForDistance(distance=library.inchToMM(7.5),DRIVE_SPEED=120,p=-.9,sensor_lf=library.colorSensor1)
    library.rightAttachment.run_angle(60, 45)
    library.driveBase.straight(library.inchToMM(-4))
    library.lineFollowForDistance(distance=library.inchToMM(11.75),DRIVE_SPEED=120,p=-.9,sensor_lf=library.colorSensor1)
    library.turn(230)
    library.driveBase.straight(library.inchToMM(9))
    library.turn(-10)
    library.driveBase.straight(library.inchToMM(-12))
    library.driveBase.straight(library.inchToMM(18))
    library.driveBase.turn(-150)
    library.driveBase.straight(library.inchToMM(-9))
    library.rightAttachment.stop()
    library.driveBase.stop()
    #library.turn(20)
"""
    library.driveBase.turn(90)
    library.driveBase.straight(library.inchToMM(-20))
    library.driveBase.turn(90)
    library.driveBase.straight(library.inchToMM(3.5))
    """