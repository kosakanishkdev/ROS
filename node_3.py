#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
     rospy.loginfo("I have got %s", data.data)

def node_3():
     rospy.init_node('nodes_3', anonymous = True)
     rospy.Subscriber("topic_2",String, callback)
     rospy.spin()
     

if __name__ == '__main__':
    node_3()
    rospy.sleep(1)
