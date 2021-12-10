#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Image, SoundFile, ImageFile

def comboFour(library):
    #Running motor until stalled to align the attachment, then stop.
    #library.rightAttachment.run_until_stalled(30)
    #library.rightAttachment.stop()
    library.rightAttachment.run_angle(-60, 40)
     #Go up to the line to line follow5
    library.driveBase.straight(library.inchToMM(6.5))
    library.turn(45, 100) 
    library.driveBase.straight(library.inchToMM(8)) 
    
    #Line follow to truck, and push it
    library.lineFollowForDistance(distance=library.inchToMM(18.25),DRIVE_SPEED=120,p=-.9,sensor_lf=library.colorSensor1)
    
    #Knock over first bridge
    library.rightAttachment.run_angle(-60, 35)
    library.lineFollowForDistance(distance=library.inchToMM(4.25),DRIVE_SPEED=120,p=-.9,sensor_lf=library.colorSensor1)
    library.rightAttachment.run_angle(-60, 35)

    #Knock over second bridge
    library.lineFollowForDistance(distance=library.inchToMM(7.5),DRIVE_SPEED=120,p=-.9,sensor_lf=library.colorSensor1)
    library.rightAttachment.run_angle(60, 55)
    library.driveBase.straight(library.inchToMM(-4))

    #Head towards crane
    library.lineFollowForDistance(distance=library.inchToMM(6.25),DRIVE_SPEED=100,p=-1.2,sensor_lf=library.colorSensor1)
    library.lineFollowForDistance(distance=library.inchToMM(5),DRIVE_SPEED=100,p=-.7,sensor_lf=library.colorSensor1)
    library.turn(-125)
    library.driveBase.straight(library.inchToMM(8.75))
    library.turn(-20)

    

    #Push the crane back, and begin getting ready to go to the Accident Avoidance
    library.driveBase.straight(library.inchToMM(-12.75))
    library.driveBase.straight(library.inchToMM(19))
    
    #Go to Accident Avoidance and knock it over.
    library.driveBase.turn(-125)
    library.driveBase.straight(library.inchToMM(-8.6))
    library.rightAttachment.stop()
    library.driveBase.stop()
"""
    library.driveBase.turn(90)
    library.driveBase.straight(library.inchToMM(-20))
    library.driveBase.turn(90)
    library.driveBase.straight(library.inchToMM(3.5))
    
"""