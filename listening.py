#!/usr/bin/python3

import rospy
from std_msgs.msg import String

rospy.init_node("the_listener_node")

def callback(msg):
	print(msg.data)

the_listener = rospy.Subscriber("/chats", String, callback)
rospy.spin()


