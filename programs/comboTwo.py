#!/usr/bin/env pybricks-micropython
from pybricks.tools import wait

def comboTwo(library):
    #Go up to the line to line follow
    library.driveBase.straight(library.inchToMM(6.5))
    library.turn(40, 100) 
    library.driveBase.straight(library.inchToMM(8.189)) 

    #line follow till bridge
    #library.lineFollowUntilShade(SHADE=93, DRIVE_SPEED=10, p=-.9)
    #lineFollow 
    library.lineFollowForDistance(distance=library.inchToMM(46.5),DRIVE_SPEED=120,p=-.9,sensor_lf=library.colorSensor1)
    library.leftAttachment.run_angle(75,-115)
    library.lineFollowForDistance(distance=library.inchToMM(9.5),DRIVE_SPEED=120,p=-.9,sensor_lf=library.colorSensor1)
    
    #strait again
    #library.driveBase.drive(library.inchToMM(1.5),22)
    #library.turn(105)

    #stop the motors
    library.leftAttachment.stop()
    library.rightAttachment.stop()
    library.driveBase.stop()