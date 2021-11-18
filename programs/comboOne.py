#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Image, SoundFile, ImageFile

def comboOne(library):
    #left medium depth container: 125mm-150mm
    #left forward container
    #left back container
  
    #center medium depth container: 139-154mm
    #center forward container
    #center back container
    library.leftAttachment.run_until_stalled(-200)
    wait(500)
    distance = library.ultrasonicSensor4.distance()
    if (distance < 150):
        if (distance > 125):
            print ("orange: " + str(distance))
        else:
            print ("green: " + str(distance))
        while True:
            library.turn(90, 200) 
            library.driveBase.straight(-115)
            library.turn(-90, 200)
            distance = library.ultrasonicSensor4.distance()
            if (distance < 150):
                if (distance > 125):
                    print ("orange: " + str(distance))
                else:
                    print ("green: " + str(distance))
            else:
                print ("blue: " + str(distance))
                break
    else:
        print ("blue: " + str(distance))
    library.leftAttachment.reset_angle(0)
    library.leftAttachment.run_target(100, 10)
