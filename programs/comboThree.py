#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Image, SoundFile, ImageFile

speed = 500

def comboThree(library):
    # make sure left attachment is in the same place every time
    library.leftAttachment.run_until_stalled(speed)
    # drive to dumpster
    library.driveBase.straight(240)
    library.lineFollowForDistance(distance = 200, sensor_lf = library.colorSensor2)
    # turn to push the dumpster off
    library.turn(-90)
    # push the dumpster off
    library.driveBase.straight(150)
    library.driveBase.straight(-150)
    library.turn(90)
    # drive to engine
    library.driveBase.straight(195)
    library.turn(40)
    # get left attachment in place by lowering it
    library.leftAttachment.reset_angle(0)
    library.leftAttachment.run_target(speed, -260)
    library.leftAttachment.hold()
    # approach engine
    library.driveBase.straight(170)
    library.turn(30)
    library.driveBase.straight(40)
    # flip engine
    library.leftAttachment.run_until_stalled(speed)
    # drive back to drop green cargo
    library.driveBase.straight(-45)
    library.turn(-40)
    library.driveBase.straight(-80)
    # drop off green cargo
    library.rightAttachment.run_until_stalled(-100)
    library.driveBase.straight(-160)
    # airplane unload
    library.leftAttachment.run_until_stalled(speed)
    library.rightAttachment.run_until_stalled(speed)
    library.turn(-90)
    library.driveBase.straight(-5)
    library.rightAttachment.run_until_stalled(-speed)
    library.rightAttachment.hold()
    library.driveBase.straight(-20)
    # go home!
    library.turn(-45)
    library.driveBase.settings(straight_speed=1000)
    library.driveBase.stop()
    library.driveBase.straight(350)
    # library.rightAttachment.stop()
    library.driveBase.stop()
    library.driveBase.settings(straight_speed=1000)




    library.leftAttachment.stop()
    library.driveBase.stop()

   # library.leftAttachment.run_target(100, -100)
