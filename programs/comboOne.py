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
    #left medium depth container: 125mm-150mm
    #left forward container
    #left back container
  
    #center medium depth container: 139-154mm
    #center forward container
    #center back container
    distance = library.ultrasonicSensor4.distance()
    if (distance < 150):
        if (distance > 125):
            print ("orange")
        else:
            print ("green")
    else:
        print ("blue")
    library.driveBase.turn(-25)
    if (distance < 154):
        if (distance > 139):
            print ("orange")
        else:
            print ("green")
    else:
        print ("blue")
