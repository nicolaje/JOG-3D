from morse.builder import *

atrv=Robot('atrv')
motion=Actuator('v_omega')
motion.translate(z=0.3)
atrv.append(motion)

pose=Sensor('pose')
pose.translate(z=0.83)
atrv.append(pose)

pose.configure_mw('socket')
pose.configure_service('socket')
motion.configure_service('socket')

env=Environment('indoors-1/indoor-1')
env.place_camera([5, -5, 6])
env.aim_camera([1.0470, 0, 0.7854])
