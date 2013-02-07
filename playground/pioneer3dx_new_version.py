from morse.builder import *

pioneer = ATRV()#Pioneer3DX()
#pioneer.unparent_wheels()

motion = MotionVW()
pioneer.append(motion)
motion.configure_service('socket')

pose = Pose()
pose.translate(x=-0.2000, z=0.9000)
pioneer.append(pose)

Keyb = Keyboard()
Keyb.properties(Speed=3.0)
pioneer.append(Keyb)

env = Environment('indoors-1/indoor-1')
env.place_camera([5, -5, 6])
env.aim_camera([1.0470, 0, 0.7854])
