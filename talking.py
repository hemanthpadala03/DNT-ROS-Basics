#!/usr/bin/python3

import rospy
from std_msgs.msg import String


rospy.init_node("the_talking_node")

the_talker = rospy.Publisher("/chats", String, queue_size=10)
rate = rospy.rate(1)
while not rospy.is_shutdown():
	data="Hello"
	the_talker.publish(data)
	rate.sleep()
	


