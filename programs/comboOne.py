#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Image, SoundFile, ImageFile

def goToNext(library):
    library.turn(90)
    library.driveBase.straight(-90)
    library.turn(-90)

def goToPrev(library):
    library.turn(90)
    library.driveBase.straight(90)
    library.turn(-90)

def comboOne(library):
    #left medium depth container: 125mm-150mm
    #left forward container
    #left back container
  
    #center medium depth container: 139-154mm
    #center forward container
    #center back container
    orangePos = -1
    greenPos = -1
    bluePos = -1

    library.leftAttachment.run_until_stalled(300)
    distance = library.ultrasonicSensor4.distance()
    if (distance < 185):
        if (distance > 150):
            print ("orange: " + str(distance))
            orangePos = 1
        else:
            print ("green: " + str(distance))
            greenPos = 1
    else:
        print ("blue: " + str(distance))
        bluePos = 1

    goToNext(library)
    distance = library.ultrasonicSensor4.distance()

    if (distance < 185):
        if (distance > 150):
            print ("orange: " + str(distance))
            orangePos = 2
        else:
            print ("green: " + str(distance))
            greenPos = 2
    else:
        print ("blue: " + str(distance))
        bluePos = 2
    
    goToNext(library)
    distance = library.ultrasonicSensor4.distance()

    if (distance < 185):
        if (distance > 150):
            print ("orange: " + str(distance))
            orangePos = 3
        else:
            print ("green: " + str(distance))
            greenPos = 3
    else:
        print ("blue: " + str(distance))
        bluePos = 3

    if (bluePos == 2):
        goToPrev(library)
    elif (bluePos == 1):
        goToPrev(library)
        goToPrev(library)
    
    library.leftAttachment.reset_angle(0)
    library.leftAttachment.run_target(300, -165)
    library.driveBase.straight(100)
    library.leftAttachment.reset_angle(0)
    library.leftAttachment.run_target(200, 120)
    library.driveBase.straight(-100)

    if (bluePos == 1): library.turn(190)
    elif (bluePos == 2): library.turn(180)
    elif (bluePos == 3): library.turn(170)

    library.driveBase.straight(300)
    library.leftAttachment.run_until_stalled(-500)
    library.driveBase.straight(-200)

    library.driveBase.stop()