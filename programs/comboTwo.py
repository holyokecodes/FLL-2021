#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Image, SoundFile, ImageFile

def comboTwo(library):
    #strait
    library.driveBase.straight(library.inchToMM(6.5))
    #turn 45 degrees 
    library.turn(40)
    #strait 
    library.driveBase.straight(library.inchToMM(10))
    #line follow till bridge
    library.lineFollowForDistance(distance=library.inchToMM(61),DRIVE_SPEED=170,p=-.9,sensor_lf=library.colorSensor1)
    #strait again
    library.driveBase.drive(library.inchToMM(3.5),22)
    wait(2000)
    library.driveBase.stop()
    library.turn(120)
    library.lineFollowForDistance(distance=library.inchToMM(6),DRIVE_SPEED=170,p=-.9,sensor_lf=library.colorSensor1)
    library.lineFollowUntilShade(SHADE=17,sensor_lf=library.colorSensor2, DRIVE_SPEED=130,p=-.9)

    #turn 60 degrees 
    #strait again
    #use attachment 
    #strait again
    #turn 60 degrees
    #strait again
    #line follow till bridge
    #strait
    #turn 45 degrees
    #strait