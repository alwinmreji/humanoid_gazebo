#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Float64
q_s = 15
negative = ['Right_Elbow','Right_Shoulder_RotX','Right_Shoulder_RotY','Right_Shoulder_RotZ']
names =  {
 'Face':rospy.Publisher('ajit/head_positon_controller/command',Float64,queue_size = q_s),
 'Left_Elbow':rospy.Publisher('ajit/left_lower_arm_position_controller/command',Float64,queue_size = q_s),
 'Left_Shoulder_RotX':rospy.Publisher('ajit/left_shoulder_joint_position_controller/command',Float64,queue_size = q_s),
 'Left_Shoulder_RotY':rospy.Publisher('ajit/left_shoulder_position_controller/command',Float64,queue_size = q_s),
 'Left_Shoulder_RotZ':rospy.Publisher('ajit/left_upper_arm_position_controller/command',Float64,queue_size = q_s),
 'Left_Wrist':rospy.Publisher('ajit/left_hand_position_controller/command',Float64,queue_size = q_s),
 'Neck':rospy.Publisher('ajit/neck_position_controller/command',Float64,queue_size = q_s),
 'Right_Elbow':rospy.Publisher('ajit/right_lower_arm_position_controller/command',Float64,queue_size = q_s),
 'Right_Shoulder_RotX':rospy.Publisher('ajit/right_shoulder_joint_position_controller/command',Float64,queue_size = q_s),
 'Right_Shoulder_RotY':rospy.Publisher('ajit/right_shoulder_position_controller/command',Float64,queue_size = q_s),
 'Right_Shoulder_RotZ':rospy.Publisher('ajit/right_upper_arm_position_controller/command',Float64,queue_size = q_s),
 'Right_Wrist':rospy.Publisher('ajit/right_hand_position_controller/command',Float64,queue_size = q_s)}


def splitter(data):
    global negative
    for i in range(len(data.name)):
        if data.name[i] in negative:
            names[data.name[i]].publish(-1*data.position[i])
        else:
            names[data.name[i]].publish(data.position[i])
        rospy.loginfo(data.name[i])
        rospy.loginfo(data.position[i])

def recive():
     rospy.init_node("reciver",anonymous=True)
     rospy.Subscriber("/dynamixel_workbench/joint_states",JointState,splitter)
     rospy.spin()
if __name__ == '__main__':
    while not rospy.is_shutdown():
        recive()
