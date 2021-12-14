#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Image, SoundFile, ImageFile

def comboOne(library):
    #goes back and forth fast to push cargo containers into a black circle
    library.driveBase.settings(straight_speed=1000)
    library.driveBase.straight(library.inchToMM(21.5))
    library.driveBase.stop()
    library.driveBase.straight(library.inchToMM(-21.5))
    library.driveBase.stop()
    library.driveBase.settings(straight_speed=100)
