#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Float64MultiArray
# q_s = 15
# negative = ['Right_Elbow','Right_Shoulder_RotX','Right_Shoulder_RotY','Right_Shoulder_RotZ']
#[head,left_lower_arm,left_shoulder_joint,left_shoulder,left_upper_arm,left_hand,neck,right_lower_arm,right_shoulder_joint,right_shoulder,right_upper_arm,right_hand]
data_pass = rospy.Publisher('ajit_2/robot_position_controller/command',Float64MultiArray,queue_size = 5)

def splitter(data):
    val = Float64MultiArray()
    # val.layout.dim = [12]
    val.data = [i*-1 for i in data.position]
    data_pass.publish(val)
    rospy.loginfo(val.data)

def recive():
     rospy.init_node("reciver",anonymous=True)
     rospy.Subscriber("/dynamixel_workbench/joint_states",JointState,splitter)
     # rospy.spin()
if __name__ == '__main__':
    recive()
    while(not rospy.is_shutdown()):
        # splitter()
        rospy.spin()
