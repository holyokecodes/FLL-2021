#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Image, SoundFile, ImageFile

def comboThree(library):
    library.driveBase.straight(500)
    library.turn(-75)
    library.driveBase.straight(200)
    library.driveBase.straight(-200)
    library.turn(75)
    library.driveBase.straight(185)
    library.turn(25)
    # library.driveBase.

    #library.rightAttachment.run_time(-150,8000)