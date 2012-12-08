#! /usr/bin/env morseexec

from morse.builder import *

robot = Robot('atrv')

waypoint = Actuator('waypoint')
robot.append(waypoint)

waypoint.configure_overlay('ros',
                           'morse.middleware.ros.overlays.actuator.WayPoint')

env = Environment('indoors-1/indoor-1')
