#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Float64MultiArray

data_pass = rospy.Publisher('ajit_2/robot_position_controller/command',Float64MultiArray,queue_size = 5)

def splitter(data):
    val = Float64MultiArray()
    val.data = [i*-1 for i in data.position]
    data_pass.publish(val)
    rospy.loginfo(val.data)

def recive():
     rospy.init_node("reciver",anonymous=True)
     rospy.Subscriber("/dynamixel_workbench/joint_states",JointState,splitter)

if __name__ == '__main__':
    recive()
    while(not rospy.is_shutdown()):
        rospy.spin()
