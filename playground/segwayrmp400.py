from morse.builder import *

# Append Pioneer robot to the scene
#robot = WheeledRobot('pioneer3dx')
#robot.rotate(z=0.73)
#robot.translate(x=-2.0, z=0.2)
#robot.unparent_wheels()


segway=WheeledRobot('pioneer3dx')
motion=Actuator('v_omega')
motion.translate(z=0.3)
segway.append(motion)
segway.unparent_wheels()

#pose=Sensor('pose')
#pose.translate(z=0.83)
#segway.append(pose)

#pose.configure_mw('socket')
#pose.configure_service('socket')
motion.add_service('socket')

env=Environment('indoors-1/indoor-1')
env.place_camera([5, -5, 6])
env.aim_camera([1.0470, 0, 0.7854])
