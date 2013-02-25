from morse.builder import *

for i in range(0,10):
	r=Robot('JOG-C.Rieux.blend')

	k=Keyboard()
	k.properties(Speed=1.0)
	r.append(k)
	r.translate(x=i)

env = Environment('indoors-1/indoor-1')
env.place_camera([5, -5, 6])
env.aim_camera([1.0470, 0, 0.7854])
