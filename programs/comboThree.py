#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Image, SoundFile, ImageFile

def comboThree(library):
    library.driveBase.straight(445)
    library.turn(-90)
    library.driveBase.straight(200)
    library.driveBase.straight(-200)
    library.turn(90)
    library.driveBase.straight(200)
    library.turn(40)
    library.driveBase.straight(170)
    library.turn(35)     
    library.leftAttachment.run_target(100, -165)
    library.leftAttachment.hold()
    library.driveBase.straight(35)
    library.leftAttachment.run_target(180, 100)
    #library.driveBase.straight(-35)
   # library.turn(-45)
    library.leftAttachment.stop()


   # library.leftAttachment.run_target(100, -100)

