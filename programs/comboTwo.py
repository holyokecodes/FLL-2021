#!/usr/bin/env pybricks-micropython
from pybricks.tools import wait
def comboTwo(library):
    #Go up to the line to line follow
    library.driveBase.straight(library.inchToMM(6.5))
    library.turn(40) 
    library.driveBase.straight(library.inchToMM(10)) 

    #line follow till bridge
    library.lineFollowForDistance(distance=library.inchToMM(61),DRIVE_SPEED=170,p=-.9,sensor_lf=library.colorSensor1)
    #strait again
    library.driveBase.drive(library.inchToMM(3.5),22)
    wait(2000)
    library.driveBase.stop()
    library.turn(120)
    library.lineFollowForDistance(distance=library.inchToMM(6),DRIVE_SPEED=170,p=-.9,sensor_lf=library.colorSensor1)
    library.lineFollowUntilShade(SHADE=17,sensor_lf=library.colorSensor2, DRIVE_SPEED=130,p=-.9)

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