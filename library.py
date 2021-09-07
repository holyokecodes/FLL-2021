#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from math import *

class FUNCTION_LIBRARY:
    def __init__(self, robot, ev3, left_motor, right_motor, medium_motor, color_sensor_1, color_sensor_2):
        #self, DriveBase, Hub
        self.driveBase = robot
        self.hub = ev3
        
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.medium_motor = medium_motor

        self.left_motor.reset_angle(0)
        self.left_motor.reset_angle(0)

        self.stopWatch = StopWatch()
        self.color_sensor_1 = color_sensor_1 
        self.color_sensor_2 = color_sensor_2

    def shutdown(self):
        self.hub.speaker.say("Logic error, error error error error error error error error error error errorrr Non halting program detected, shutting down")
        #self.hub.speaker.say("Shutting down...")
        self.hub.speaker.play_notes(['C4/4', 'F3/4', 'F2/4'])

    def line_follow_until_black(self, p=1.2, DRIVE_SPEED=100, BLACK=9, WHITE= 85, sensor_lf=-1, sensor_stop=-1,  debug=False):
        if (sensor_lf == -1):
            sensor_lf = self.color_sensor_1
        if (sensor_stop == -1):
            sensor_stop = self.color_sensor_2 

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

    def line_follow_until_white(self, p=1.2, DRIVE_SPEED=100, BLACK=9, WHITE= 85, sensor_lf=-1, sensor_stop=-1,  debug=False):
        if (sensor_lf == -1):
            sensor_lf = self.color_sensor_1
        if (sensor_stop == -1):
            sensor_stop = self.color_sensor_2 # I NEED TO CREATE NEW CONSTANt

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


    def line_follow_for_time(self, p=1, DRIVE_SPEED=100, BLACK=9, WHITE= 85, sensor_lf=-1, time=10000, debug=False):
        if (sensor_lf == -1):
            sensor_lf = self.color_sensor_2
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

    def line_follow_for_distance(self, p=1, DRIVE_SPEED=100, BLACK=9, WHITE= 85, sensor_lf=-1, distance=10000, debug=False):
        #BLACK = 9 #what is black
        #WHITE = 85 #what is white, also what is life (42)
        if (sensor_lf == -1):
            sensor_lf = self.color_sensor_2
        elif (sensor_lf == -2):
            sensor_lf = self.color_sensor_1
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

    def mm_to_inch(self, mm):
        return mm/25.4
    def inch_to_mm(self, inch):
        return inch*25.4
    def ms_to_second(self, ms):
        return ms/1000
    def second_to_ms(self, s):
        return s*1000

        