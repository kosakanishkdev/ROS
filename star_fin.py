#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def move():
	rospy.init_node("move", anonymous = True)
	pub = rospy.Publisher("/turtle1/cmd_vel",Twist, queue_size = 10)
	rate = rospy.Rate(1)
	v = Twist()


	for i in range(6):
		v.linear.x = 2.0
		v.linear.y = 0.0
		v.angular.z = 0.0
		pub.publish(v)
		rate.sleep()

		v.linear.x = 0.0
		v.linear.y = 0.0
		v.angular.z = 2.51
		pub.publish(v)
		rate.sleep()

if __name__== '__main__':
	move()