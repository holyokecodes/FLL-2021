#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Image, SoundFile, ImageFile

def comboFour(library):
    #Running motor to prevent it being too high
    library.rightAttachment.run_angle(-60, 40)
     
    #Go up to the line to line follow
    library.driveBase.straight(library.inchToMM(6.5))
    library.turn(42, 100) 
    library.driveBase.straight(library.inchToMM(8)) 
    
    #Line follow to truck, and push it
    library.lineFollowForDistance(distance=library.inchToMM(18.25),DRIVE_SPEED=120,p=-.9,sensor_lf=library.colorSensor1)

    #Knock over first bridge
    library.rightAttachment.run_angle(-60, 35)
    library.lineFollowForDistance(distance=library.inchToMM(4.25),DRIVE_SPEED=120,p=-.7,sensor_lf=library.colorSensor1)
    library.rightAttachment.run_angle(-60, 35)

    #Knock over second bridge
    library.lineFollowForDistance(distance=library.inchToMM(7.5),DRIVE_SPEED=120,p=-.7,sensor_lf=library.colorSensor1)
    library.rightAttachment.run_angle(60, 55)
    library.driveBase.straight(library.inchToMM(-4))

    #Head towards cargo connect circle
    library.lineFollowForDistance(distance=library.inchToMM(6.25),DRIVE_SPEED=100,p=-1.2,sensor_lf=library.colorSensor1)
    library.lineFollowForDistance(distance=library.inchToMM(5),DRIVE_SPEED=100,p=-.7,sensor_lf=library.colorSensor1)
    library.turn(160)
    library.driveBase.straight(80)
    library.leftAttachment.run_angle(60,-115)

    #Head towards crane
    library.turn(80)
    library.driveBase.stop()
    library.driveBase.settings(straight_speed=250)
    library.driveBase.straight(235)
    library.turn(-32)
    library.driveBase.stop()
    library.driveBase.settings(straight_speed=500)
    library.driveBase.straight(-360)

    #Go to Accident Avoidance and knock it over.
    library.driveBase.straight(500)
    library.driveBase.stop()
    library.driveBase.settings(straight_speed=100)
    library.turn(-125)
    library.driveBase.straight(library.inchToMM(-8.75))

    #stop the motors
    library.leftAttachment.stop()
    library.rightAttachment.stop()
    library.driveBase.stop()
    