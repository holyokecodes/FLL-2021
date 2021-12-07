#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Image, SoundFile, ImageFile

def comboThree(library):
    # make sure left attachment is in the same place every time
    library.leftAttachment.run_until_stalled(100)
    # drive to dumpster
    library.driveBase.straight(445)
    # turn to push the dumpster off
    library.turn(-90)
    # push the dumpster off
    library.driveBase.straight(130)
    library.driveBase.straight(-130)
    library.turn(90)
    # drive to engine
    library.driveBase.straight(185)
    library.turn(45)
    # get left attachment in place 
    library.leftAttachment.reset_angle(0)
    library.leftAttachment.run_target(100, -260)
    library.leftAttachment.hold()
    # approach engine
    library.driveBase.straight(165)
    library.turn(25)
    library.driveBase.straight(60)
    library.turn(15)
    # flip engine
    library.leftAttachment.run_until_stalled(100)
    # drive back to drop green cargo
    library.driveBase.straight(-45)
    library.turn(-40)
    library.driveBase.straight(-80)
    # drop off green cargo
    library.rightAttachment.run_until_stalled(-100)
    library.driveBase.straight(-170)
    # airplane unload
    library.leftAttachment.run_until_stalled(100)
    library.rightAttachment.run_until_stalled(100)
    library.turn(-95)
    library.driveBase.straight(-5)
    library.rightAttachment.run_until_stalled(-100)
    library.driveBase.straight(-20)
    # go home!
    library.turn(-45)
    library.driveBase.straight(350)





    library.leftAttachment.stop()
    library.driveBase.stop()

   # library.leftAttachment.run_target(100, -100)
