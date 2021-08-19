#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
     rospy.loginfo("I have got the message from node_1",data.data)


def node_2():
	pub = rospy.Publisher("topic_2",String,queue_size = 10)
	rospy.Subscriber("topic_1",String, callback)
	rospy.init_node("node_2", anonymous = True)
	rate = rospy.Rate(1)

	while not rospy.is_shutdown():
		message = "this is the message from node_2"
		rospy.loginfo(message)
		pub.publish(message)
		rate.sleep()

if __name__ == '__main__':
	node_2()
