#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Image, SoundFile, ImageFile

def comboThree(library):
    library.leftAttachment.run_until_stalled(100)
    library.driveBase.straight(445)
    library.turn(-90)
    library.driveBase.straight(130)
    library.driveBase.straight(-130)
    library.turn(90)
    library.driveBase.straight(230)
    library.turn(37)
    library.leftAttachment.reset_angle(0)
    library.leftAttachment.run_target(100, -260)
    library.leftAttachment.hold()
    library.driveBase.straight(165)
    library.turn(25)
    library.driveBase.straight(20)
    library.leftAttachment.run_until_stalled(100)
    library.driveBase.straight(-45)
    library.turn(-25)
    library.driveBase.straight(-20)
    library.leftAttachment.stop()
    library.driveBase.stop()

   # library.leftAttachment.run_target(100, -100)

