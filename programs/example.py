#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from library import FuctionLibrary


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
motorA = Motor(Port.A)

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Calibrate your drive base.
# You can also just measure everything

# This should drive 100 mm straight forward.
# If it doesn't go far enough, decrease your wheel_diameter.
# If it goes too far, increase your wheel diameter.
# When it is perfect, comment this code out.
#robot.straight(100)

# This should turn 360 degrees.
# If it turns less than 360 degrees, increase the axle_track
# If it turns more than 360 degrees, decrease the axle_track
# When it is perfect, comment this code out.
#robot.turn(360)

# Go forward and backwards for one meter.
#robot.straight(1000)
# robot.drive(speed=150, turn_rate=60)
# wait(1000)
# robot.stop()
ev3.speaker.beep()
ev3.speaker.play_file(SoundFile.HELLO)
ev3.speaker.say("I can say anything!")
ev3.speaker.play_notes(['C4/4', 'G4/4'])
ev3.screen.draw_text(50, 60, "Hello!")
wait(1000)

# Calibrate your drive base.
# You can also just measure everything

# This should drive 100 mm straight forward.
# If it doesn't go far enough, decrease your wheel_diameter.
# If it goes too far, increase your wheel diameter.
# When it is perfect, comment this code out.
#robot.straight(100)

# This should turn 360 degrees.
# If it turns less than 360 degrees, increase the axle_track
# If it turns more than 360 degrees, decrease the axle_track
# When it is perfect, comment this code out.
#robot.turn(360)

# Go forward and backwards for one meter.
#robot.straight(1000)
# robot.drive(speed=150, turn_rate=60)
# wait(1000)
# robot.stop()
#ev3.speaker.beep()
#ev3.speaker.play_file(SoundFile.HELLO)
#ev3.speaker.say("Logic error, error error error error error error error error error error errorrr Non halting program detected, shutting down")
#ev3.speaker.play_notes(['C4/4', 'F3/4', 'F2/4'])

#library.shutDown()

#ev3.screen.draw_text(50, 60, "Hello!")
#wait(1000)

#use the library

#library.line_follow_for_time(p=2, sensor=sensor_b)

# library.shutdown()