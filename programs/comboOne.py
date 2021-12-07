#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Image, SoundFile, ImageFile

def goToNext(library):
    library.turn(-90)
    library.driveBase.straight(-90)
    library.turn(80)

def goToPrev(library, times=1):
    library.turn(-90)
    for i in range(times):
        library.driveBase.straight(90)
    library.turn(100)

def goToCorrectPos(library, tartgetPos):
    if tartgetPos == 3: goToNext(library)
    elif tartgetPos == 2: pass
    elif tartgetPos == 1: goToPrev(library)

def pickUp(library):
    library.leftAttachment.reset_angle(0)
    library.leftAttachment.run_target(300, 100)
    library.driveBase.straight(100)
    library.leftAttachment.reset_angle(0)
    library.leftAttachment.run_target(200, -100)
    library.driveBase.straight(-100)

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

    library.leftAttachment.run_until_stalled(-300)
    library.rightAttachment.run_until_stalled(300)

    distance = library.infraredSensor4.distance()
    if (distance < 13):
        if (distance >= 10):
            print ("orange: " + str(distance))
            if orangePos == -1: orangePos = 1
        else:
            print ("green: " + str(distance))
            if greenPos == -1: greenPos = 1
    else:
        print ("blue: " + str(distance))
        if bluePos == -1: bluePos = 1

    library.turn(-10)
    library.driveBase.straight(-30)
    library.turn(-80)
    library.driveBase.straight(-100)
    library.turn(90)
    library.driveBase.straight(10)

    distance = library.infraredSensor4.distance()
    
    if (distance < 14):
        if (distance > 11):
            print ("orange: " + str(distance))
            if orangePos == -1: orangePos = 2
        else:
            print ("green: " + str(distance))
            if greenPos == -1: greenPos = 2
    else:
        print ("blue: " + str(distance))
        if bluePos == -1: bluePos = 2

    if (orangePos == 1 and greenPos == 2):
        bluePos = 3
        print("O: 1, G: 2, therefore, B:3")
    if (orangePos == 2 and greenPos == 1):
        bluePos = 3
        print("O: 2, G: 1, therefore, B:3")

    if (bluePos == 1 and greenPos == 2):
        orangePos = 3
        print("B: 1, G: 2, therefore, O:3")
    if (bluePos == 2 and greenPos == 1):
        orangePos = 3
        print("B: 2, G: 1, therefore, O:3")

    if (orangePos == 1 and bluePos == 2):
        greenPos = 3
        print("O: 1, B: 2, therefore, G:3")
    if (orangePos == 2 and bluePos == 1):
        greenPos = 3
        print("O: 2, B: 1, therefore, G:3")

    print(bluePos)
    
    goToCorrectPos(library, bluePos)

    if(bluePos == 3): library.turn(10)
    pickUp(library)

    if (bluePos == 1):
        library.turn(-30)
        library.driveBase.straight(-100)
        library.turn(195)
        library.driveBase.straight(140)
    if (bluePos == 2):
        library.turn(175)
        library.driveBase.straight(200)

    library.leftAttachment.run_until_stalled(500)
    library.driveBase.straight(-200)
