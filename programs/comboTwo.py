#!/usr/bin/env pybricks-micropython
from pybricks.tools import wait

def comboTwo(library):
    #Go up to the line to line follow
    library.driveBase.straight(library.inchToMM(6.5))
    library.turn(40, 100) 
    library.driveBase.straight(library.inchToMM(8.189)) 

    #Line follow until the  circle, then drop container
    library.lineFollowForDistance(distance=library.inchToMM(46.5),DRIVE_SPEED=120,p=-.9,sensor_lf=library.colorSensor1)
    library.leftAttachment.run_angle(75,-115)

    #Line follow into the air drop
    library.lineFollowForDistance(distance=library.inchToMM(9.5),DRIVE_SPEED=120,p=-.9,sensor_lf=library.colorSensor1)

    #Stop the motors
    library.leftAttachment.stop()
    library.rightAttachment.stop()
    library.driveBase.stop()