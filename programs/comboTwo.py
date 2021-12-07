#!/usr/bin/env pybricks-micropython
from pybricks.tools import wait

def comboTwo(library):
    #Go up to the line to line follow
    library.leftAttachment.run_target(100, -50, wait=False)
    library.leftAttachment.hold()
    library.rightAttachment.run_target(100, -50, wait=False)
    library.rightAttachment.hold()

    library.turn(-15)
    library.driveBase.straight(90)
    library.turn(-40)
    library.driveBase.straight(320)
    return 

    #line follow till bridge
    #library.lineFollowUntilShade(SHADE=93, DRIVE_SPEED=10, p=-.9)
    #lineFollow 
    library.lineFollowForDistance(distance = library.inchToMM(48), DRIVE_SPEED = 120, p = -0.9, sensor_lf = library.colorSensor1)
    #strait again
    library.driveBase.drive(library.inchToMM(3.5),22)
    wait(2000)
    library.driveBase.stop()
    library.turn(85)
    library.lineFollowForDistance(distance=library.inchToMM(8),p=-.9)
    library.lineFollowUntilShade(SHADE=17,p=-.9, tolerance=1)
    library.lineFollowForDistance(distance=library.inchToMM(2),p=-.9)
    
    #turn 60 degrees 
    #strait again
    #use attachment 
    #strait again
    #turn 60 degrees
    #strait again
    #line follow till bridge
    #strait
    #turn 45 degrees
    #strait