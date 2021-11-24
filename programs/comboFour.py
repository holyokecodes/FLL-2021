#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Image, SoundFile, ImageFile

def comboFour(library):
    while True:
        print("Untrasonic Sensor" + str(library.ultrasonicSensor.distance()))
        print("Color Sensor 2" + str(library.colorSensor2.reflection()))
        print("Color Sensor 1" + str(library.colorSensor1.reflection()))
