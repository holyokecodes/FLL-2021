#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Image, SoundFile, ImageFile
from time import sleep

from math import *

class FUNCTION_LIBRARY:
    def __init__(self, robot, ev3, leftDriveMotor, rightDriveMotor, leftAttachment, rightAttachment, colorSensor1, colorSensor2, gyroscope3, gyroscope4):
        #self, DriveBase, Hub
        self.driveBase = robot
        self.hub = ev3
        
        self.leftDriveMotor = leftDriveMotor
        self.rightDriveMotor = rightDriveMotor
        self.leftAttachment = leftAttachment
        self.rightAttachment = rightAttachment

        self.leftDriveMotor.reset_angle(0)
        self.rightDriveMotor.reset_angle(0)

        self.stopWatch = StopWatch()

        self.colorSensor1 = colorSensor1 
        self.colorSensor2 = colorSensor2
        self.gyroscope3 = gyroscope3
        self.gyroscope4 = gyroscope4

        self.black = 9
        self.white = 85

        self.gyro3Drift = False
        self.gyro4Drift = False

    #PURPOSE: Calibrates robot
    #PARAMS: None
    def calibrate(self):
        self.checkGyroscopes()
        self.calibrateColors()
    
    #PURPOSE: Calibrates Gyroscopes
    #PARAMS: None
    def checkGyroscopes(self):
        if self.gyroscope3 != -1: self.gyroscope3.reset_angle(0)
        if self.gyroscope4 != -1: self.gyroscope4.reset_angle(0)

        try: print("Gyro 3 Angle First: " + str(self.gyroscope3.angle()))
        except: print("Gyro 3 Angle First: [Error]")
        try: print("Gyro 4 Angle First: " + str(self.gyroscope4.angle()))
        except: print("Gyro 4 Angle First: [Error]")

        sleep(1)

        try: print("Gyro 3 Angle Second: " + str(self.gyroscope3.angle()))
        except: print("Gyro 3 Angle Second: [Error]")
        try: print("Gyro 4 Angle Second: " + str(self.gyroscope4.angle()))
        except: print("Gyro 4 Angle Second: [Error]")

        if self.gyroscope3 != -1: self.gyro3Drift = (self.gyroscope3.angle() != 0)
        else: self.gyro3Drift = True

        if self.gyroscope4 != -1: self.gyro4Drift = (self.gyroscope4.angle() != 0)
        else: self.gyro4Drift = True

        print("Gyro 3 Drift: " + str(self.gyro3Drift))
        print("Gyro 4 Drift: " + str(self.gyro4Drift))
    
    #PURPOSE: Calibrates Color Sensors
    #PARAMS: None
    def callibrateColors(self):
        blackDone = False
        whiteDone = False

        print("old black: " + str(self.black) + ", old white: " + str(self.white))
        self.hub.screen.load_image(Image('GUI/ColorCalibrateNone.PNG'))
        while True:
            if Button.LEFT in self.hub.buttons.pressed() and not blackDone:
                self.black = (self.colorSensor1.reflection() + self.colorSensor2.reflection()) / 2
                if (whiteDone): self.hub.screen.load_image(Image('GUI/ColorCalibrateBoth.PNG'))
                else: self.hub.screen.load_image(Image('GUI/ColorCalibrateBlack.PNG'))
                blackDone = True

            if Button.RIGHT in self.hub.buttons.pressed() and not whiteDone:
                self.white = (self.colorSensor1.reflection() + self.colorSensor2.reflection()) / 2
                if (blackDone): self.hub.screen.load_image(Image('GUI/ColorCalibrateBoth.PNG'))
                else: self.hub.screen.load_image(Image('GUI/ColorCalibrateWhite.PNG'))
                whiteDone = True
                
            if blackDone and whiteDone:
                sleep(1)
                break

        print("new black: " + str(self.black) + ", new white: " + str(self.white))

    #PURPOSE: Line follows until it finds a certain shade of B&W (0 is black, 100 is white)
    #PARAMS: 
    #p: https://youtu.be/AMBWV_HGYj4?t=212
    #DRIVE_SPEED: How fast the robot should go.
    #BLACK: Black to determine treshold: https://youtu.be/AMBWV_HGYj4?t=90.
    #WHITE: White to determine treshold: https://youtu.be/AMBWV_HGYj4?t=90.
    #SHADE: Shade to stop at.
    #sensor_lf: Sensor to line follow with.
    #sensor_stop: Sensor to determine when to stop.
    #debug: Turns on print statements to see what the sensor_lf is seeing.

    def lineFollowUntilShade(self, p=1.2, DRIVE_SPEED=100, BLACK=9, WHITE= 85, SHADE=-1, sensor_lf=-1, sensor_stop=-1,  debug=False):
        if (sensor_lf == -1):
            sensor_lf = self.colorSensor1
        if (sensor_stop == -1):
            sensor_stop = self.colorSensor2 
        if (SHADE == -1):
            print("ERROR: Please define the shade that you'll be using.")
        PROPORTIONAL_GAIN = p
        threshold = (BLACK + WHITE) / 2 #the average/mean of black+white

        while True: #forever, do
            if (debug):
                print(sensor_lf.reflection()) #how bright the stuff the color sensor sees is
            #Calculate the turn rate from the devation and set the drive base speed and turn rate.
            self.driveBase.drive(DRIVE_SPEED, PROPORTIONAL_GAIN * (sensor_lf.reflection() - threshold))
            
            #stop condition 
            if sensor_stop.reflection() <= SHADE: 
                self.driveBase.stop()
                break

    #PURPOSE: Line follows until a timer finishes
    #PARAMS: 
    #p: https://youtu.be/AMBWV_HGYj4?t=212
    #DRIVE_SPEED: How fast the robot should go.
    #BLACK: Black to determine treshold: https://youtu.be/AMBWV_HGYj4?t=90.
    #WHITE: White to determine treshold: https://youtu.be/AMBWV_HGYj4?t=90.
    #sensor_lf: Sensor to line follow with.
    #time: How long the timer should go for in milliseconds (1/1000 of a second).
    #debug: Turns on print statements to see what the sensor_lf is seeing and to say how long the timer went for.
    def lineFollowForTime(self, p=1, DRIVE_SPEED=100, BLACK=9, WHITE= 85, sensor_lf=-1, time=10000, debug=False):
        if (sensor_lf == -1):
            sensor_lf = self.colorSensor2
        self.stopWatch.reset()
        self.stopWatch.resume()

        PROPORTIONAL_GAIN = p
        #BLACK = 9 #what is black
        #WHITE = 85 #what is white, also what is life (42)
        threshold = (BLACK + WHITE) / 2 #the center of black+white

        while True: #forever, do

            if (debug):
                print(sensor_lf.reflection()) #how bright the stuff the color sensor sees is
            #Calculate the turn rate from the devation and set the drive base speed and turn rate.
            self.driveBase.drive(DRIVE_SPEED, PROPORTIONAL_GAIN * (sensor_lf.reflection() - threshold))
            
            #stop condition 
            if self.stopWatch.time() > time: 
                break 

        self.driveBase.stop()
        if debug:
            self.hub.speaker.say("I line followed for" + str(floor(time/1000)) + "seconds")
    
    #PURPOSE: Line follows until the robot has gone a certain distance
    #PARAMS: 
    #p: https://youtu.be/AMBWV_HGYj4?t=212
    #DRIVE_SPEED: How fast the robot should go.
    #BLACK: Black to determine treshold: https://youtu.be/AMBWV_HGYj4?t=90.
    #WHITE: White to determine treshold: https://youtu.be/AMBWV_HGYj4?t=90.
    #SHADE: Shade to stop at.
    #sensor_lf: Sensor to line follow with.
    #distance: Distance to stop at in millimeters (1/1000 of a meter or 25.4 millimeters per inch)
    #debug: Turns on print statements to see what the sensor_lf is seeing.
    def lineFollowForDistance(self, p=1, DRIVE_SPEED=100, BLACK=9, WHITE= 85, sensor_lf=-1, distance=10000, debug=False):
        if (sensor_lf == -1):
            sensor_lf = self.colorSensor2
        elif (sensor_lf == -2):
            sensor_lf = self.colorSensor1
        PROPORTIONAL_GAIN = p
        threshold = (BLACK + WHITE) / 2 #the center of black+white
        startingDistance = self.driveBase.distance()
        while True: #forever, do
            if (debug):
                print(sensor_lf.reflection()) #how bright the stuff the color sensor sees is
            #Calculate the turn rate from the devation and set the drive base speed and turn rate.
            self.driveBase.drive(DRIVE_SPEED, PROPORTIONAL_GAIN * (sensor_lf.reflection() - threshold))
            
            #stop condition 
            if self.driveBase.distance()-startingDistance > distance: 
                break 
        self.driveBase.stop()

    #PURPOSE: Turns the robot.
    #PARAMS:
    #degrees: The number of degrees the robot turned.
    #speed: The speed the robot turns at in mm/s.
    def turn(self, degrees, speed=100):
        turnMode = ""
        if (self.gyro3drift and self.gyro4drift):
            turnMode = "No GYRO"
        elif (self.gyro3drift and not self.gyro4drift):
            turnMode = "GYRO4"
        elif (not self.gyro3drift and self.gyro4drift):
            turnMode = "GYRO3"
        elif (not self.gyro3drift and not self.gyro4drift):
            turnMode = "GYRO"
        
        print(turnMode)

        # if turnmode == "NO GYRO":
        #     self.driveBase.turn(degrees)
        self.driveBase.turn(degrees)
    
    def mmToInch(self, mm):
        return mm/25.4
    def inchToMM(self, inch):
        return inch*25.4
    def msToSecond(self, ms):
        return ms/1000
    def secondToMS(self, s):
        return s*1000