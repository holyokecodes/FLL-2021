#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

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

    def shutdown(self):
        self.hub.speaker.say("Logic error, error error error error error error error error error error errorrr Non halting program detected, shutting down")
        #self.hub.speaker.say("Shutting down...")
        self.hub.speaker.play_notes(['C4/4', 'F3/4', 'F2/4'])

    def calibrate(self):
        self.checkGyroscopes()
        self.calibrateColors()
    
    def checkGyroscopes(self):
        self.gyroscope3.resetAngle(0)
        self.gyroscope4.resetAngle(0)
        self.robot.sleep(1)
        self.gyro3Drift = self.gyroscope3.angle != 0
        self.gyro4Drift = self.gyroscope4.angle != 0

    def callibrateColors(self):
        numbersDone = 0
        print("old black: " + self.black + ", old white: " + self.white)
        while True:
            if Button.LEFT in self.hub.buttons.pressed():
                self.black = (self.colorSensor1.reflection() + self.colorSensor2.reflection()) / 2
                numbersDone += 1

            if Button.RIGHT in self.hub.buttons.pressed():
                self.white = (self.colorSensor1.reflection() + self.colorSensor2.reflection()) / 2
                numbersDone += 1
            
            if numbersDone == 2:
                break
        print("new black: " + self.black + ", new white: " + self.white)

    def lineFollowUntilBlack(self, p=1.2, DRIVE_SPEED=100, BLACK=9, WHITE= 85, sensor_lf=-1, sensor_stop=-1,  debug=False):
        if (sensor_lf == -1):
            sensor_lf = self.colorSensor1
        if (sensor_stop == -1):
            sensor_stop = self.colorSensor2 

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
            if sensor_stop.reflection() <= BLACK: #
                self.driveBase.stop()
                break #thrillitup

    def lineFollowUntilWhite(self, p=1.2, DRIVE_SPEED=100, BLACK=9, WHITE= 85, sensor_lf=-1, sensor_stop=-1,  debug=False):
        if (sensor_lf == -1):
            sensor_lf = self.colorSensor1
        if (sensor_stop == -1):
            sensor_stop = self.colorSensor2 # I NEED TO CREATE NEW CONSTANt

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
            if sensor_stop.reflection() <= WHITE: #
                self.driveBase.stop()
                break #thrillitup


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
            if self.stopWatch.time() > time: #
                break #STOP THIEF

        self.driveBase.stop()
        self.hub.speaker.say("I line followed for" + str(floor(time/1000)) + "seconds")

    def lineFollowForDistance(self, p=1, DRIVE_SPEED=100, BLACK=9, WHITE= 85, sensor_lf=-1, distance=10000, debug=False):
        #BLACK = 9 #what is black
        #WHITE = 85 #what is white, also what is life (42)
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
            if self.driveBase.distance()-startingDistance > distance: #
                break #STOP THIEF
        self.driveBase.stop()
        ##self.hub.speaker.say("I have reached " + str(floor(distance/25.4)) + "inches") removed this, pauses robot too long

    def turn(self, degrees, speed=100):
        turnMode = ""
        if (self.gyro3drift and self.gyro4drift):
            turn(degrees)
        elif (self.gyro3drift and not self.gyro4drift):
            turnMode = "GYRO4"
        elif (not self.gyro3drift and self.gyro4drift):
            turnMode = "GYRO3"
        elif (not self.gyro3drift and not self.gyro4drift):
            turnMode = "GYRO"


    def mmToInch(self, mm):
        return mm/25.4
    def inchToMM(self, inch):
        return inch*25.4
    def msToSecond(self, ms):
        return ms/1000
    def secondToMS(self, s):
        return s*1000