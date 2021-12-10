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
    #goes back and forth fast to push three cargo containers into a black circle
    library.driveBase.settings(straight_speed=1000)
    library.driveBase.straight(library.inchToMM(21.5))
    library.driveBase.stop()
    library.driveBase.straight(library.inchToMM(-21.5))
    library.driveBase.stop()
    library.driveBase.settings(straight_speed=100)
    #power and the money,
    #money and the power,
    #day after day 
    #hour after hour