from morse.builder import *

ir_update_freq=2;
sonar_update_freq=2;
compass_update_freq=2;
odo_update_freq=2;
pose_update_freq=2;

odometer_x=0.1
odometer_y=0.135

see_sonar_arcs=True
see_infrared_arcs=True

front_side_sonar_theta=15*2*3.14/360
sonar_z=0.095
front_side_side_sonar_x=0.08
front_side_side_sonar_y=0.195

front_side_sonar_x=0.082
front_side_sonar_y=0.135

sonar_range=3 # I presume

infrared_z=0.09
infrared_side_y=0.12
infrared_side_x=-0.11
infrared_back_x=-0.19
infrared_range=0.3 # According to the datasheet

r=Robot('JOG-C.Rieux.blend')
k=Keyboard()
k.properties(Speed=1.0)
r.append(k)

# Sensors initialization
irLeft=Infrared()
irLeft.properties(laser_range=infrared_range)
irLeft.frequency(ir_update_freq)
irFront=Infrared()
irFront.properties(laser_range=infrared_range)
irFront.frequency(ir_update_freq)
irRight=Infrared()
irRight.properties(laser_range=infrared_range)
irRight.frequency(ir_update_freq)
irBack=Infrared()
irBack.properties(laser_range=infrared_range)
irBack.frequency(ir_update_freq)

sonarLeftLeft=Infrared()
sonarLeftLeft.properties(laser_range=sonar_range)
sonarLeftLeft.frequency(sonar_update_freq)
sonarLeft=Infrared()
sonarLeft.properties(laser_range=sonar_range)
sonarLeft.frequency(sonar_update_freq)
sonarFront=Infrared()
sonarFront.properties(laser_range=sonar_range)
sonarFront.frequency(sonar_update_freq)
sonarRight=Infrared()
sonarRight.properties(laser_range=sonar_range)
sonarRight.frequency(sonar_update_freq)
sonarRightRight=Infrared()
sonarRightRight.properties(laser_range=sonar_range)
sonarRightRight.frequency(sonar_update_freq)

pose=Pose()
pose.frequency(pose_update_freq)

odometerLeft=Odometry()
odometerLeft.frequency(odo_update_freq)
odometerRight=Odometry()
odometerRight.frequency(odo_update_freq)

# Sonar sensors positioning
sonarLeftLeft.properties(Visible_arc=see_sonar_arcs)
sonarLeftLeft.translate(z=sonar_z, x=front_side_side_sonar_x, y=front_side_side_sonar_y)
sonarLeftLeft.rotate(z=front_side_sonar_theta)

sonarLeft.properties(Visible_arc=see_sonar_arcs)
sonarLeft.translate(z=sonar_z,x=front_side_sonar_x,y=front_side_sonar_y)

sonarFront.properties(Visible_arc=see_sonar_arcs)
sonarFront.translate(x=front_side_sonar_x+0.05,y=0)

sonarRight.properties(Visible_arc=see_sonar_arcs)
sonarRight.translate(z=sonar_z,x=front_side_sonar_x,y=-front_side_sonar_y)

sonarRightRight.properties(Visible_arc=see_sonar_arcs)
sonarRightRight.translate(z=sonar_z, x=front_side_side_sonar_x, y=-front_side_side_sonar_y)
sonarRightRight.rotate(z=-front_side_sonar_theta)

# Infrared sensors positioning
irFront.properties(Visible_arc=see_infrared_arcs)
irFront.translate(z=infrared_z, x=front_side_sonar_x)

irLeft.properties(Visible_arc=see_infrared_arcs)
irLeft.translate(y=infrared_side_y,z=infrared_z,x=infrared_side_x)
irLeft.rotate(z=90*3.14/180)

irRight.properties(Visible_arc=see_infrared_arcs)
irRight.translate(y=-infrared_side_y,z=infrared_z,x=infrared_side_x)
irRight.rotate(z=-90*3.14/180)

irBack.properties(Visible_arc=see_infrared_arcs)
irBack.translate(x=infrared_back_x,z=infrared_z)
irBack.rotate(z=-3.14)

# Odometer sensors positioning
# using default level (integration) that
# we will cut down into ticks on Java side
odometerLeft.translate(x=odometer_x,y=odometer_y)
odometerRight.translate(x=odometer_x,y=-odometer_y)
odometerRight.level('integrated')
odometerLeft.level('integrated')

# Actuator
actuator=MotionVW()
actuator.translate(x=odometer_x)

# Configuring socket datastreams
sonarLeftLeft.add_stream('socket')
sonarLeft.add_stream('socket')
sonarFront.add_stream('socket')
sonarRight.add_stream('socket')
sonarRightRight.add_stream('socket')

irLeft.add_stream('socket')
irRight.add_stream('socket')
irFront.add_stream('socket')
irBack.add_stream('socket')

pose.add_stream('socket')

odometerLeft.add_stream('socket')
odometerRight.add_stream('socket')

actuator.add_stream('socket')

# Attaching sensors to the robot
r.append(sonarLeftLeft)
r.append(sonarLeft)
r.append(sonarFront)
r.append(sonarRight)
r.append(sonarRightRight)

r.append(irFront)
r.append(irLeft)
r.append(irRight)
r.append(irBack)

r.append(pose)

r.append(odometerLeft)
r.append(odometerRight)

r.append(actuator)

env = Environment('indoors-1/indoor-1')
env.place_camera([5, -5, 6])
env.aim_camera([1.0470, 0, 0.7854])
