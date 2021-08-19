#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def node_1():
	pub = rospy.Publisher("topic_1",String,queue_size = 10)
	rospy.init_node("node_1", anonymous = True)
	rate = rospy.Rate(1)

	while not rospy.is_shutdown():
		message = "this is the message from node_1"
		rospy.loginfo(message)
		pub.publish(message)
		rate.sleep()

if __name__ == '__main__':
	node_1()
