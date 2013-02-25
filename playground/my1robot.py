from morse.builder import *

robot = Robot('my1robot.blend')

k=Keyboard()
k.properties(Speed=1.0)
robot.append(k)

env = Environment('indoors-1/indoor-1')
