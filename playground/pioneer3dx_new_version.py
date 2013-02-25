from morse.builder import *

atrv=ATRV()
atrv.translate(x=-1, y=0.4)

ir1=Infrared()
ir1.properties(Visible_arc=True)
ir1.translate(x=0, y=0, z=0.9)
ir1.properties(resolution=5)
ir1.properties(scan_window=90)
ir1.properties(laser_range=5.0)
atrv.append(ir1)

k=Keyboard()
k.properties(Speed=3.0)
atrv.append(k)

env = Environment('indoors-1/indoor-1')
env.place_camera([5, -5, 6])
env.aim_camera([1.0470, 0, 0.7854])
