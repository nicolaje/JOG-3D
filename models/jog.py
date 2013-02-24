from morse.builder import *

r=Robot('JOG-C.Rieux.blend')

k=Keyboard()
k.properties(Speed=1.0)
r.append(k)

env = Environment('indoors-1/indoor-1')
env.place_camera([5, -5, 6])
env.aim_camera([1.0470, 0, 0.7854])
