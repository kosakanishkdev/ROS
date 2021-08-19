#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def node_1():
	rospy.init_node("node_1",anonymous = True)
	pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size = 10)
	rate = rospy.Rate(10)
	vel = Twist()

	while not rospy.is_shutdown():
		vel.linear.x = 5.0
		
                rate.sleep()
		pub.publish(vel)

if __name__ == '__main__':
    node_1()

