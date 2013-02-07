#!/usr/bin/python

from morse.builder.morsebuilder import *

robot = Robot('my1robot.blend')

motion = Actuator('v_omega')
robot.append(motion)
motion.add_stream('socket')

env = Environment('indoors-1/indoor-1')
