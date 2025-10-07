#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import JointState
from brics_actuator.msg import JointPositions, JointValue

ARM_JOINT_NAMES = [
    'arm_joint_1',
    'arm_joint_2',
    'arm_joint_3',
    'arm_joint_4',
    'arm_joint_5'
]

joint_positions = [0.0] * 5
joint_positions_updated = False
# Joint limitleri tanımla
JOINT_LIMITS = {
    'arm_joint_1': (0.0100692, 5.84014),
    'arm_joint_2': (0.0100692, 2.61799),
    'arm_joint_3': (-5.02655, -0.015708),
    'arm_joint_4': (0.0221239, 3.4292),  
    'arm_joint_5': (0.110619, 5.64159)
}

def get_joint_input(joint_num):
    joint_name = f"arm_joint_{joint_num}"
    min_val, max_val = JOINT_LIMITS[joint_name]
    while True:
        val = float(input(f"Joint {joint_num} için açı değeri girin (limit: {min_val:.4f} ile {max_val:.4f} rad): "))
        if min_val <= val <= max_val:
            return val
        print(f"UYARI: Değer limit dışında! {min_val:.4f} ile {max_val:.4f} arasında bir değer girin.")

def joint_state_callback(msg):
    global joint_positions, joint_positions_updated
    if not joint_positions_updated:
        # Check if message contains arm joints (first 5 positions)
        if len(msg.position) >= 5 and msg.name[0].startswith('arm_joint'):
            joint_positions = list(msg.position[:5])  # İlk 5 pozisyonu al
            joint_positions_updated = True

def create_joint_positions_msg(joint_names, joint_positions):
    msg = JointPositions()
    for name, pos in zip(joint_names, joint_positions):
        jv = JointValue()
        jv.timeStamp.secs = 0
        jv.timeStamp.nsecs = 0
        jv.joint_uri = name
        jv.unit = "rad"
        jv.value = pos
        msg.positions.append(jv)
    return msg

def send_joint_positions():
    rospy.init_node('joint_position_publisher', anonymous=True)
    rospy.Subscriber('/joint_states', JointState, joint_state_callback)
    pub = rospy.Publisher('/arm_1/arm_controller/position_command', JointPositions, queue_size=10)

    while not joint_positions_updated and not rospy.is_shutdown():
        rospy.sleep(0.1)

    print("Mevcut joint açıları:")
    for i, pos in enumerate(joint_positions, 1):
        print(f"Joint {i}: {pos:.4f}")

    print("1-5: Sadece ilgili joint\n6: Tüm jointler")
    secim = int(input("Seçiminiz (1-6): "))

    if 1 <= secim <= 5:
        val = get_joint_input(secim)
        joint_positions[secim-1] = val
    elif secim == 6:
        for i in range(5):
            val = get_joint_input(i+1)
            joint_positions[i] = val
    else:
        print("Geçersiz seçim!")
        return

    msg = create_joint_positions_msg(ARM_JOINT_NAMES, joint_positions)
    pub.publish(msg)
    rospy.loginfo(f"Gönderilen joint açıları: {joint_positions}")

if __name__ == '__main__':
    try:
        send_joint_positions()
    except rospy.ROSInterruptException:
        pass